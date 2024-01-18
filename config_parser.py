from configparser import ConfigParser

# Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

# Get the port
userinfo = config_object["SERVERCONFIG"]


def get_port():
    return int(userinfo["port"])


if __name__ == "__main__":
    print("port is {}".format(userinfo["port"]))
