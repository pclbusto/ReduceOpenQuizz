#|
$JSON
{"authURL":["ai2.appinventor.mit.edu"],"YaVersion":"213","Source":"Form","Properties":{"$Name":"scrPlay","$Type":"Form","$Version":"30","AppName":"ICanBelieveIt","Title":"Play","TitleVisible":"False","TutorialURL":"https:\/\/islegmar.github.io\/appinventor_icanbelieveit\/help.html","Uuid":"0","$Components":[{"$Name":"lyMain","$Type":"VerticalArrangement","$Version":"4","Width":"-2","Uuid":"764129775","$Components":[{"$Name":"lyConfigClient","$Type":"VerticalArrangement","$Version":"4","Width":"-2","Uuid":"-295184674","Visible":"False","$Components":[{"$Name":"HorizontalArrangement4","$Type":"HorizontalArrangement","$Version":"4","Height":"20","Width":"-2","Uuid":"-1957637531"},{"$Name":"Label5","$Type":"Label","$Version":"5","FontBold":"True","FontSize":"22","Width":"-2","Text":"Chose the Server :","Uuid":"-2010125051"},{"$Name":"lpConnect","$Type":"ListPicker","$Version":"9","Text":"Chose Server","Uuid":"-373731363","Visible":"False"},{"$Name":"lvConnect","$Type":"ListView","$Version":"6","BackgroundColor":"&HFFCCCCCC","TextColor":"&HFF000000","Uuid":"-2090456695"}]},{"$Name":"lyConfigServer","$Type":"VerticalArrangement","$Version":"4","Width":"-2","Uuid":"-1520551683","Visible":"False","$Components":[{"$Name":"HorizontalScrollArrangement1","$Type":"HorizontalScrollArrangement","$Version":"2","Height":"20","Width":"-2","Uuid":"1590080933"},{"$Name":"Label4","$Type":"Label","$Version":"5","FontBold":"True","FontSize":"22","Text":"Waiting clients to connect ...","Uuid":"-716599749"},{"$Name":"bStartPlay","$Type":"Button","$Version":"7","Text":"Start","Uuid":"279319068"},{"$Name":"lblClientsConnected","$Type":"Label","$Version":"5","BackgroundColor":"&HFFCCCCCC","FontSize":"18","Height":"300","Width":"-2","Uuid":"2064877663"}]},{"$Name":"lyWaiting2Play","$Type":"HorizontalArrangement","$Version":"4","Width":"-2","Uuid":"-1668821758","Visible":"False","$Components":[{"$Name":"Label3","$Type":"Label","$Version":"5","FontBold":"True","FontSize":"22","Width":"-2","Text":"Waiting for game to start ...","Uuid":"22600904"}]},{"$Name":"lyPlay","$Type":"VerticalArrangement","$Version":"4","Height":"-2","Width":"-2","Uuid":"-24450730","Visible":"False","$Components":[{"$Name":"VerticalArrangement1","$Type":"VerticalArrangement","$Version":"4","Width":"-2","Uuid":"-150168861","$Components":[{"$Name":"HorizontalArrangement3","$Type":"HorizontalArrangement","$Version":"4","Uuid":"-1442300857","$Components":[{"$Name":"txPoints","$Type":"TextBox","$Version":"6","FontBold":"True","Hint":"Hint for TextBox1","NumbersOnly":"True","ReadOnly":"True","Text":"0","Uuid":"-523116421"},{"$Name":"txTime","$Type":"TextBox","$Version":"6","FontBold":"True","Hint":"Hint for TextBox1","NumbersOnly":"True","ReadOnly":"True","Text":"0","Uuid":"-613387229"}]},{"$Name":"txtQuestion","$Type":"TextBox","$Version":"6","FontSize":"22","Height":"-1030","Width":"-2","MultiLine":"True","ReadOnly":"True","Uuid":"1960543646"},{"$Name":"lyAnswerMultiple","$Type":"TableArrangement","$Version":"1","Width":"-2","Uuid":"-887669490","$Components":[{"$Name":"bAns1","$Type":"Button","$Version":"7","Column":"0","Width":"-1050","Row":"0","Uuid":"-2142465206"},{"$Name":"bAns2","$Type":"Button","$Version":"7","Column":"1","Width":"-1050","Row":"0","Uuid":"1404492840"},{"$Name":"bAns3","$Type":"Button","$Version":"7","Column":"0","Row":"1","Uuid":"1862191380"},{"$Name":"bAns4","$Type":"Button","$Version":"7","Column":"1","Row":"1","Uuid":"1286953453"}]}]}]}]},{"$Name":"lyDebug","$Type":"VerticalArrangement","$Version":"4","Width":"-2","Uuid":"828722009","$Components":[{"$Name":"HorizontalArrangement5","$Type":"HorizontalArrangement","$Version":"4","Width":"-2","Uuid":"706156884","$Components":[{"$Name":"bCleanDebug","$Type":"Button","$Version":"7","Text":"Clean","Uuid":"878743715"},{"$Name":"bSwitchDebug","$Type":"Button","$Version":"7","Uuid":"564572637"}]},{"$Name":"txDebug","$Type":"TextBox","$Version":"6","Width":"-2","Hint":"Hint for TextBox1","MultiLine":"True","Uuid":"-1437059844"},{"$Name":"lyInfo","$Type":"TableArrangement","$Version":"1","Columns":"6","Width":"-2","Rows":"4","Uuid":"597049255","$Components":[{"$Name":"cbIsServer","$Type":"CheckBox","$Version":"2","Column":"0","Row":"0","Text":"Server?","Uuid":"-854260406"},{"$Name":"cbSinglePlayer","$Type":"CheckBox","$Version":"2","Column":"1","Row":"0","Text":"Single Player?","Uuid":"-605940766"},{"$Name":"cbIAmHost","$Type":"CheckBox","$Version":"2","Column":"2","Row":"0","Text":"I am Host?","Uuid":"1299180097"},{"$Name":"cbTimerRemain","$Type":"CheckBox","$Version":"2","Column":"0","Row":"1","Text":"TRemain?","Uuid":"-12855022"},{"$Name":"cbTimerReceiver","$Type":"CheckBox","$Version":"2","Column":"1","Row":"1","Text":"TReceiver?","Uuid":"1793820841"},{"$Name":"cbTimerQuestion","$Type":"CheckBox","$Version":"2","Column":"2","Row":"1","Text":"TQuestion?","Uuid":"1301239290"},{"$Name":"cbIAnswered","$Type":"CheckBox","$Version":"2","Column":"0","Row":"2","Text":"IAnswered?","Uuid":"2051356669"},{"$Name":"txNumberQ","$Type":"TextBox","$Version":"6","Column":"0","Width":"20","Hint":"Hint for TextBox1","NumbersOnly":"True","ReadOnly":"True","Row":"3","Uuid":"1400187998"},{"$Name":"txIndChosen","$Type":"TextBox","$Version":"6","Column":"1","Width":"20","Hint":"Hint for TextBox1","NumbersOnly":"True","ReadOnly":"True","Row":"3","Uuid":"496187815"},{"$Name":"lblAnswer","$Type":"Label","$Version":"5","Column":"2","Height":"-2","Row":"3","Uuid":"426350872"}]}]},{"$Name":"webJSON","$Type":"Web","$Version":"8","Uuid":"648280396"},{"$Name":"timeRemaining","$Type":"Clock","$Version":"4","TimerAlwaysFires":"False","TimerEnabled":"False","TimerInterval":"0","Uuid":"-10566008"},{"$Name":"blueClient","$Type":"BluetoothClient","$Version":"6","Uuid":"-1579241488"},{"$Name":"blueServer","$Type":"BluetoothServer","$Version":"5","Uuid":"-1551189766"},{"$Name":"timerReceiver","$Type":"Clock","$Version":"4","TimerAlwaysFires":"False","TimerEnabled":"False","TimerInterval":"100","Uuid":"-1694331924"},{"$Name":"Notifier1","$Type":"Notifier","$Version":"6","Uuid":"-1970577389"},{"$Name":"timerShowQuestion","$Type":"Clock","$Version":"4","TimerAlwaysFires":"False","TimerEnabled":"False","TimerInterval":"2000","Uuid":"-35477062"},{"$Name":"timerDebug","$Type":"Clock","$Version":"4","TimerAlwaysFires":"False","Uuid":"-1004139139"},{"$Name":"db","$Type":"TinyDB","$Version":"2","Uuid":"-1267917427"}]}}
|#