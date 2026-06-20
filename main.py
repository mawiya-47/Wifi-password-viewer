import subprocess
import re

def get_wifi_profiles():
    output = subprocess.check_output(
        ["netsh", "wlan", "show", "profiles"],
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    profiles = re.findall(r"All User Profile\s*:\s(.*)", output)
    return profiles

def get_wifi_password(profile):
    try:
        output = subprocess.check_output(
            ["netsh", "wlan", "show", "profile", profile, "key=clear"],
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        match = re.search(r"Key Content\s*:\s(.*)", output)
        return match.group(1) if match else "No Password Found"

    except:
        return "Error"

def main():
    print("\nSaved Wi-Fi Passwords\n")
    print("-" * 50)

    for profile in get_wifi_profiles():
        password = get_wifi_password(profile)
        print(f"WiFi Name : {profile}")
        print(f"Password  : {password}")
        print("-" * 50)

if __name__ == "__main__":
    main()
