f = open("/SSHS/codes/Batch/Networks.txt", "r", encoding = "utf-8")
networks = f.readlines()
f.close()

networks = [i.split(":")[1].strip() for i in networks if "All User Profile" in i]

f = open("/SSHS/codes/Batch/Networks.txt", "w", encoding = "utf-8")

f.write("\n".join(networks))

f.close()