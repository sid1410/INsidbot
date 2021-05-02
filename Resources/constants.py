headers = {
"authority":"www.chegg.com",
"accept":"application/json; charset=UTF-8",
"accept-encoding":"gzip, deflate, br",
"accept-language":"en-US,en;q=0.9",
"dnt":"1",
"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
}
headers_tbs = {
"authority":"www.chegg.com",
"path": "/schema/_ajax,persistquerygraphql",
"accept":"application/json",
"content-Type": "application/json",
"accept-encoding":"gzip, deflate, br",
"accept-language":"en-US,en;q=0.5",
"TE":"Trailers",
"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
'dnt':"1",
"pragma":'no-cache'
}

tbs_template = "<html><head></head><body>" \
            "<div style='border:double;border-width:medium;background-color: #ff8533'> " \
                "<p style='font-size: 20px;font-weight: bold;'>For more answers</p>"\
               " <a href='https://t.me/sid_chegg_bot'>Click Here</a> "\
               "</div>" \
            "<p style='font-size: 20px;font-weight: bold;'>Question</p>" \
           "<div style='border:double;border-width:medium;background-color:lightgreen'>{}</div>" \
           "<p style='font-size: 20px;font-weight: bold;'>Solution</p>" \
            "<div style='border:double;border-width:medium;background-color: lightblue'>"

step_html = "<p style='font-size: 20px;font-weight: bold;'><mark>Step-{}</mark></p>"
tbs_end_template = "</div>" \
        "<div style='border:double;border-width:medium;background-color: yellow'>" \
           "<p><b>Likes: {} </b></p>" \
           "<p><b>Dislikes: {}</b>" \
           "</div>" \
           "</body></html>"

template = "<html><head></head><body>" \
"<div style='border:double;border-width:medium;background-color: #ff8533'> " \
                "<p style='font-size: 20px;font-weight: bold;'>For more answers</p>"\
               " <a href='https://t.me/sid_chegg_bot'>Click Here</a> "\
               "</div>" \
           "<p style='font-size: 20px;font-weight: bold;'>Question</p>" \
           "<div style='border:double;border-width:medium;background-color:lightgreen'>{}</div>" \
           "<p style='font-size: 20px;font-weight: bold;'>Solution</p>" \
           "<div style='border:double;border-width:medium;background-color: lightblue'>{}</div>" \
           "<div style='border:double;border-width:medium;background-color: yellow'>" \
           "<p><b>Likes: {} </b></p>" \
           "<p><b>Dislikes: {}</b>" \
           "</div>" \
           "</body></html>"


captcha_error = "Captcha error. Please contact @Lucifer_7999"
wrong_link = "Join the Channel @sidchegg7999 and Probably wrong link. Please retry with correct link\nIf error persists contact @Lucifer_7999"
update_id = 1
bot_error = "Bot needs maintenance.\nPlease report to @Lucifer_7999\nSorry for inconvenience"
error_text = "Join the Channel @sidchegg7999 and It's an error or unsolved problem.\nPlease check once, if you think bot is culprit then contact @Lucifer_7999"
pack_expiry_message = "Join the Channel @sidchegg7999 and Your pack has been expired please recharge to continue\nKeep Chegging  😊"
unable_to_fetch = "Join the Channel @sidchegg7999 and Sorry Unable to fetch the answer ! Please try with different link"
dont_worry_msg = "Join the Channel @sidchegg7999 and Don't worry you have unlimited solutions\nKeep using the bot 😊"
solution_count_msg = "Join the Channel @sidchegg7999 and Remaining Solution: "
pack_details = """Hello! Welcome to the Chegg solutions bot. 
Use Bot @sid_chegg_bot.

Prices for solutions in Indian Rupees ₹:
📌 No. of solutions      ➡     Rates
🔹  01 solution            ➡      10  ₹
🔹  05 solutions          ➡      30  ₹
🔹  10 solutions          ➡      50  ₹
🔹  25 solutions          ➡      100  ₹
🔹  55 solutions          ➡      200  ₹
🔹  100 solutions        ➡      320  ₹

Prices for solutions in USD $:
📌 No. of solutions      ➡     Rates
🔹  30 solutions          ➡      2.0 $

Please register to bot using /register command.

Use /count to check remaining solutions.

For payment: @Lucifer_7999

If bot take more than 10 minutes, it will refund the solution automatic. 
Join the Channel @sidchegg7999 for more updates & offers.

contact: @Lucifer_7999 for any quarries or suggestions.

Thank You!🌞"""
late_message = "Join the Channel @sidchegg7999 and Sorry your solution is delayed.\nYour Solution count has been refunded please check using /count"