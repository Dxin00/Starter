import re
text = "pfdpfovpfdl 51651651 ffsdfsvs 56165165 sdfsdfsdfsdf151sdfsdfss 651651 sdvsdv"
res=re.findall("\\d+", text)
print(res)