
guest=3
while guest > 0:
	pw=input("請輸入密碼：")
	if pw == "0725":
		print("登入成功")
		break
	else:
		guest = guest - 1
		if guest == 0:
			print("密碼輸入錯誤已達三次，檔案銷毀中~~")
		else:
			print("密碼錯誤! 還有",guest,"次機會")


