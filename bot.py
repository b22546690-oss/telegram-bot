from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# তোমার Bot Token এখানে বসাও
BOT_TOKEN = "8801340067:AAHfr7kYq_wBP1dzbtgP8XRI2xi8B45LYS0"


# /start কমান্ড
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user.first_name

    text = f"""
╔══❖•ೋ° 🌸 °ೋ•❖══╗
      🤖 হেল্প সেন্টার বট
╚══❖•ೋ° 🌸 °ೋ•❖══╝

👋 আসসালামু আলাইকুম {user}

আমি একটি Telegram Help Bot ✅

এখান থেকে আপনি জানতে পারবেনঃ

📌 বটের সকল কমান্ড
📌 GitHub এ Upload System
📌 Render Hosting Guide
📌 24/7 Bot Hosting
📌 Owner Support

নিচের বাটনগুলো ব্যবহার করুন 👇
"""

    keyboard = [
        [InlineKeyboardButton("📚 সকল কমান্ড", callback_data="commands")],
        [InlineKeyboardButton("🌐 Hosting Guide", callback_data="hosting")],
        [InlineKeyboardButton("💻 GitHub System", callback_data="github")],
        [InlineKeyboardButton("🆘 সাপোর্ট", callback_data="support")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(text, reply_markup=reply_markup)


# Callback buttons
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "commands":
        text = """
📚 সকল কমান্ড

/start - বট চালু করুন
/help - সাহায্য দেখুন
/ping - বট অনলাইন কিনা দেখুন
/about - বট সম্পর্কে জানুন
"""

    elif data == "hosting":
        text = """
🌐 Hosting Guide

1️⃣ GitHub এ কোড আপলোড করুন
2️⃣ Render এ GitHub connect করুন
3️⃣ Deploy চাপুন

🚀 24/7 bot online থাকবে
"""

    elif data == "github":
        text = """
💻 GitHub System

1️⃣ Repository তৈরি করুন
2️⃣ bot.py upload করুন
3️⃣ requirements.txt যোগ করুন
4️⃣ Render deploy করুন
"""

    elif data == "support":
        text = """
🆘 Support

👨‍💻 Owner: @YourUsername
📩 সমস্যা হলে message করুন
"""

    else:
        text = "Invalid option"

    await query.message.reply_text(text)


# /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📌 /start ব্যবহার করুন")


# /ping
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Bot online আছে ✅")


# /about
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
🤖 Bot Info

📌 Python Telegram Bot
📌 Hosting Ready
📌 Simple & Fast
"""
    await update.message.reply_text(text)


# ================= MAIN SYSTEM =================

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CallbackQueryHandler(buttons))

    print("✅ Bot Running Successfully...")

    app.run_polling()


# ✅ ENTRYPOINT FIX (এটাই তোমার error fix করবে)
if __name__ == "__main__":
    main()
