import c2m_email

mail_token_jongho = ['wfjo852@gmail.com','odtizpmqcumaitnm']
mail_token_meta = ['meta360@c2monster.com','kwadnrquhhjghrep']


# file_result = c2m_email.file(r'H:\Park_doc\python\C2M_mail\meta360.pdf')
html_result = c2m_email.html(r'H:\Park_doc\python\C2M_mail\html\test.html')

c2m_email.mail_send(mail_token=mail_token_jongho,
                    to='wfjo852@gmail.com',
                    sub_text="추천!! 전문 의료기관과 공동 개발한 비대면 인지훈련 프로그램",
                    msg_text="",
                    html_return=html_result)
                    # file_return=file_result)
print("mail_send")

## 메일 리스트 불러오기


# mail_file = open('./email_list.txt','r')
# mail_data = mail_file.read()
# mail_list = mail_data.splitlines()
#
# for to_mail in mail_list:
#     print(to_mail +">> sended")
#     c2m_email.mail_send(mail_token=mail_token_meta,
#                         to=to_mail,
#                         sub_text="추천!! 전문 의료기관과 공동 개발한 비대면 인지훈련 프로그램",
#                         msg_text="",
#                         html_return=html_result,
#                         file_return=file_result)
#
