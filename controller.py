import time
# from honeypot_1 import HONEYPOT_1
# from honeypot_2 import HONEYPOT_2
# from honeypot_3 import HONEYPOT_3
# from honeypot_4 import HONEYPOT_4
# from honeypot_5 import HONEYPOT_5
# from honeypot_6 import HONEYPOT_6


def CONTROLLER():
    print("Honeypot Controller started, booting up honeypot instances")
    time.sleep(0.5)


def HONEYPOT_INSTANCE_1():
    print("[CONTROLLER] Starting honeypot_user_1...")
    time.sleep(0.2)
    print("[CONTROLLER] honeypot_user_1 successfully started.")
    # HONEYPOT_1()
    time.sleep(0.5)


def HONEYPOT_INSTANCE_2():
    print("[CONTROLLER] Starting honeypot_user_1...")
    time.sleep(0.2)
    print("[CONTROLLER] honeypot_user_2 successfully started.")
    # HONEYPOT_2()
    time.sleep(0.5)


def HONEYPOT_INSTANCE_3():
    print("[CONTROLLER] Starting honeypot_user_1...")
    time.sleep(0.2)
    print("[CONTROLLER] honeypot_user_3 successfully started.")
    # HONEYPOT_3()
    time.sleep(0.5)


def HONEYPOT_INSTANCE_4():
    print("[CONTROLLER] Starting honeypot_user_1...")
    time.sleep(0.2)
    print("[CONTROLLER] honeypot_user_4 successfully started.")
    # HONEYPOT_4()
    time.sleep(0.5)


def HONEYPOT_INSTANCE_5():
    print("[CONTROLLER] Starting honeypot_user_1...")
    time.sleep(0.2)
    print("[CONTROLLER] honeypot_user_5 successfully started.")
    # HONEYPOT_5()
    time.sleep(0.5)


def HONEYPOT_INSTANCE_6():
    print("[CONTROLLER] Starting honeypot_user_1...")
    time.sleep(0.2)
    print("[CONTROLLER] honeypot_user_6 successfully started.")
    # HONEYPOT_6()
    time.sleep(0.5)


if __name__ == "__main__":
    CONTROLLER()
    HONEYPOT_INSTANCE_1()
    HONEYPOT_INSTANCE_2()
    HONEYPOT_INSTANCE_3()
    HONEYPOT_INSTANCE_4()
    HONEYPOT_INSTANCE_5()
    HONEYPOT_INSTANCE_6()
