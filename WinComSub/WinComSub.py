import subprocess

print("Минимальный путь:",min(list(int(open("data.txt", "r").readlines()[1].strip())+sum(list(int(open("data.txt", "r").readlines()[2 + i].split()[0]) for i in range(int(open("data.txt", "r").readlines()[0].strip())))[0:i])+sum(list(int(open("data.txt", "r").readlines()[2 + i].split()[1]) for i in range(int(open("data.txt", "r").readlines()[0].strip())))[i:int(open("data.txt", "r").readlines()[0].strip())]) for i in range(int(open("data.txt", "r").readlines()[0].strip())+1))))

if input("Очистить консоль?y/n: ")=="y":
    subprocess.Popen("cls", shell=True).wait()
