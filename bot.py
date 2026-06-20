import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    CallbackQueryHandler, ContextTypes, filters
)
from database import Database
from analyzer import analyze_match
from datetime import datetime

# ═══════════════════════════════════════════
#              إعدادات البوت
# ═══════════════════════════════════════════
BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
ADMIN_ID = int(os.environ.get("ADMIN_ID", "123456789"))
BARIDIMOB_NUMBER = os.environ.get("BARIDIMOB_NUMBER", "0XXXXXXXXX")
SUBSCRIPTION_PRICE = 1000
SUBSCRIPTION_DAYS = 7

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

db = Database()

# ═══════════════════════════════════════════
#              أوامر المستخدم
# ═══════════════════════════════════════════

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    db.add_user(user.id, user.username or user.first_name)

    keyboard = [
        [InlineKeyboardButton("📊 تحليل مباراة", callback_data="analyze")],
        [InlineKeyboardButton("💳 الاشتراك - 1000 دج/أسبوع", callback_data="subscribe")],
        [InlineKeyboardButton("📋 حالة اشتراكي", callback_data="status")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"⚽ *مرحباً بك في بوت Bola!*\n\n"
        f"🤖 أنا بوت ذكاء اصطناعي متخصص في تحليل المباريات الرياضية\n"
        f"📈 أقدم توقعات دقيقة بناءً على تحليل تكتيكي متقدم\n\n"
        f"⚠️ *تنبيه:* التوقعات للاستفادة التحليلية فقط ولا تضمن أي نتيجة\n\n"
        f"اختر ما تريد:",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def subscribe_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_subscribe(update.message, update.effective_user.id)

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_status(update.message, update.effective_user.id)

async def analyze_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not db.is_subscribed(user_id):
        await update.message.reply_text(
            "🔒 *هذه الميزة للمشتركين فقط!*\n\n"
            "اشترك الآن بـ 1000 دج/أسبوع للوصول الكامل\n"
            "استخدم /subscribe للاشتراك",
            parse_mode="Markdown"
        )
        return

    args = context.args
    if not args or "vs" not in " ".join(args).lower():
        await update.message.reply_text(
            "📝 *طريقة الاستخدام:*\n\n"
            "`/analyze الفريق الأول vs الفريق الثاني`\n\n"
            "مثال:\n"
            "`/analyze Real Madrid vs Barcelona`",
            parse_mode="Markdown"
        )
        return

    full_text = " ".join(args)
    parts = full_text.lower().split("vs")
    team1 = parts[0].strip().title()
    team2 = parts[1].strip().title() if len(parts) > 1 else "Unknown"

    msg = await update.message.reply_text("⏳ جاري التحليل التكتيكي...")

    result = await analyze_match(team1, team2)

    await msg.edit_text(result, parse_mode="Markdown")

# ═══════════════════════════════════════════
#              أوامر الأدمن
# ═══════════════════════════════════════════

async def activate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    if not context.args:
        await update.message.reply_text("الاستخدام: /activate USER_ID")
        return

    target_id = int(context.args[0])
    db.activate_subscription(target_id, SUBSCRIPTION_DAYS)

    await update.message.reply_text(f"✅ تم تفعيل اشتراك المستخدم {target_id} لمدة {SUBSCRIPTION_DAYS} يوماً")

    try:
        await context.bot.send_message(
            chat_id=target_id,
            text="🎉 *تم تفعيل اشتراكك بنجاح!*\n\n"
                 f"✅ اشتراكك فعّال لمدة {SUBSCRIPTION_DAYS} يوماً\n"
                 "استخدم `/analyze فريق1 vs فريق2` لتحليل أي مباراة\n\n"
                 "شكراً لثقتك في بوت Bola ⚽",
            parse_mode="Markdown"
        )
    except:
        pass

async def users_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    users = db.get_all_users()
    if not users:
        await update.message.reply_text("لا يوجد مستخدمون بعد")
        return

    text = "👥 *قائمة المستخدمين:*\n\n"
    for u in users:
        status = "✅ مشترك" if u[3] else "❌ غير مشترك"
        text += f"• ID: `{u[0]}` | {u[1]} | {status}\n"

    await update.message.reply_text(text, parse_mode="Markdown")

# ═══════════════════════════════════════════
#              Callback Handlers
# ═══════════════════════════════════════════

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "subscribe":
        await show_subscribe(query.message, query.from_user.id)
    elif query.data == "status":
        await show_status(query.message, query.from_user.id)
    elif query.data == "analyze":
        await query.message.reply_text(
            "📝 *لتحليل مباراة:*\n\n"
            "أرسل الأمر بهذا الشكل:\n"
            "`/analyze فريق1 vs فريق2`\n\n"
            "مثال:\n"
            "`/analyze PSG vs Bayern Munich`",
            parse_mode="Markdown"
        )

async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """استقبال صور إيصالات الدفع"""
    user = update.effective_user
    caption = update.message.caption or ""

    await update.message.reply_text(
        "📨 *تم استلام إيصال الدفع!*\n\n"
        "⏳ سيتم مراجعته وتفعيل اشتراكك خلال ساعات قليلة\n"
        "شكراً لثقتك في بوت Bola ⚽",
        parse_mode="Markdown"
    )

    # إرسال الإيصال للأدمن
    try:
        await context.bot.forward_message(
            chat_id=ADMIN_ID,
            from_chat_id=update.effective_chat.id,
            message_id=update.message.message_id
        )
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"💳 *طلب اشتراك جديد!*\n\n"
                 f"👤 المستخدم: {user.first_name}\n"
                 f"🆔 ID: `{user.id}`\n"
                 f"📝 ملاحظة: {caption}\n\n"
                 f"لتفعيل الاشتراك:\n`/activate {user.id}`",
            parse_mode="Markdown"
        )
    except:
        pass

# ═══════════════════════════════════════════
#              دوال مساعدة
# ═══════════════════════════════════════════

async def show_subscribe(message, user_id):
    if db.is_subscribed(user_id):
        exp = db.get_expiry(user_id)
        await message.reply_text(
            f"✅ *أنت مشترك بالفعل!*\n\n"
            f"📅 ينتهي اشتراكك: {exp}\n\n"
            f"استخدم `/analyze فريق1 vs فريق2` للتحليل",
            parse_mode="Markdown"
        )
        return

    await message.reply_text(
        f"💳 *الاشتراك في بوت Bola*\n\n"
        f"💰 السعر: *{SUBSCRIPTION_PRICE} دج / شهر*\n\n"
        f"📲 *خطوات الدفع عبر بريدي موب:*\n"
        f"1️⃣ افتح تطبيق بريدي موب\n"
        f"2️⃣ أرسل {SUBSCRIPTION_PRICE} دج إلى الرقم:\n"
        f"   `{BARIDIMOB_NUMBER}`\n"
        f"3️⃣ التقط صورة للإيصال\n"
        f"4️⃣ أرسل الصورة هنا مباشرة\n\n"
        f"⏰ سيتم تفعيل اشتراكك خلال ساعات قليلة\n\n"
        f"⚠️ *ملاحظة:* التوقعات للاستفادة التحليلية فقط",
        parse_mode="Markdown"
    )

async def show_status(message, user_id):
    subscribed = db.is_subscribed(user_id)
    if subscribed:
        exp = db.get_expiry(user_id)
        await message.reply_text(
            f"📋 *حالة اشتراكك:*\n\n"
            f"✅ الحالة: *فعّال*\n"
            f"📅 ينتهي في: *{exp}*\n\n"
            f"استمتع بالتحليل التكتيكي! ⚽",
            parse_mode="Markdown"
        )
    else:
        await message.reply_text(
            f"📋 *حالة اشتراكك:*\n\n"
            f"❌ الحالة: *غير مشترك*\n\n"
            f"اشترك الآن بـ {SUBSCRIPTION_PRICE} دج/شهر\n"
            f"استخدم /subscribe",
            parse_mode="Markdown"
        )

# ═══════════════════════════════════════════
#              تشغيل البوت
# ═══════════════════════════════════════════

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # أوامر المستخدم
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("subscribe", subscribe_command))
    app.add_handler(CommandHandler("status", status_command))
    app.add_handler(CommandHandler("analyze", analyze_command))

    # أوامر الأدمن
    app.add_handler(CommandHandler("activate", activate_command))
    app.add_handler(CommandHandler("users", users_command))

    # Callbacks
    app.add_handler(CallbackQueryHandler(button_handler))

    # استقبال الصور (إيصالات الدفع)
    app.add_handler(MessageHandler(filters.PHOTO, photo_handler))

    print("🤖 بوت Bola يعمل الآن...")
    app.run_polling()

if __name__ == "__main__":
    main()
