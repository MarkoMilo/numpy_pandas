try:
    f = open("demofile.txt", mode='a')
    try:
        f.write("Marko M\n")
    except:
        print("Problem when writting to the file")
    finally:
        f.close()
except:
    print("Problem with opening file")
finally:
    f = open("demofile.txt", "a+")
    f.close()