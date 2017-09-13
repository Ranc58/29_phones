import daemon
from fix_phonenumbers import daemonize_normalize_phones


if __name__ == "__main__":
    with daemon.DaemonContext():
        daemonize_normalize_phones()
