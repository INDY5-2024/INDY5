from smtplib import SMTP
import datetime

debuglevel = 0

smtp = SMTP()
smtp.set_debuglevel(debuglevel)
smtp.connect('COVERED DUE TO PRIVACY', 26)
smtp.login('USERNAME@DOMAIN', 'PASSWORD')

from_addr = "Patrick O'Connell <my@email.net>"
to_addr = "example@bar.com"

subj = "hello"
date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )

message_text = "The Player wearing this helmet (HELMET ID) has suffered a concussion level of force. Please remove him from the game and run concussion protocol"

msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" 
        % ( from_addr, to_addr, subj, date, message_text )

smtp.sendmail(from_addr, to_addr, msg)
smtp.quit()
