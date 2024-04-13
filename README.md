<div align="center">

# Discord Honeypot System - CONCEPT

The Discord Honeypot System is a sophisticated monitoring tool designed to enhance server security and moderation efficiency. Utilizing multiple Discord accounts, each running in dedicated Virtual Machines (VMs) or Docker containers, this Python-based system automates the surveillance of direct message (DM) activity. Its primary objective is to detect, capture, and relay suspicious or unwanted DM communications to a specific channel within a designated server for further action by the moderation team.

</div>

<div align="center">

## ☕ [Support my work on Ko-Fi](https://ko-fi.com/thatsinewave)

</div>

## Key Features

- **DM Monitoring:** Automatically captures screenshots of DMs, sender profiles, and other critical information.
- **Information Gathering:** Collects sender's profile picture URL, username, nickname, UserID, mutual servers, exact message time (epoch time), and full message contents.
- **Dynamic Profile Customization:** Honeypot accounts can change their profile picture, username, nickname, about me section, pronouns, profile background color, status, and rich presence at user-defined intervals to maintain a low profile and attract different target groups.
- **Scalability:** Designed to efficiently scale from a few accounts to more than 10, ensuring adaptability to various operation sizes.

## Structure

- `controller.py`: This is the main script that starts and monitors the honeypot instances.
- `honeypot_1.py` to `honeypot_6.py`: These are honeypot instance scripts.
- `Tools folder`: Includes generator scripts to create fake data for each honeypot instance based on the `wordlist.txt` file.
- `wordlist.txt`: The generator scripts use this file to generate randomized usernames and nicknames for the honeypot accounts.
- `Honeypot-Logs folder`: Contains log files for each honeypot instance: `honeypot_log_1.json` to `honeypot_log_6.json`.
- `Tokens folder`: Contains tokens and IDs for each honeypot instance: `token_1.json` to `token_6.json`.
- `Database folder`: Contains profile images and configuration files for each honeypot instance.

## Capabilities

The system's honeypot bots are equipped with various customization abilities to enhance their effectiveness and remain undetectable. Additionally, the new controller.py script manages and monitors the honeypot instances.

1. **Profile Picture:** Randomly changes from a list of 1,000 curated images.
2. **Username & Nickname:** Randomly changes from a list of 10,000 curated usernames and nicknames.
3. **About Me Sections:** Randomly changes from a list of 10,000 curated texts.
4. **Pronouns Sections:** Randomly changes from a list of 1,000 curated texts.
5. **Profile Background Color:** Randomly selects from a wide range of color values.
6. **Status Updates:** Switches between online, away, do not disturb, and offline statuses.
7. **Rich Presence:** Simulates activity such as playing a game from a list of 100 curated titles (Not finished).

## Documentation for Honeypot Instance Files

Each honeypot instance file, such as `honeypot_1.py` to `honeypot_6.py`, serves as a standalone script responsible for simulating user behavior, monitoring direct messages (DMs), and maintaining a low-profile presence within Discord servers. Here's an overview of the functionality and structure of these files:

### Functionality:

1. **Connection Establishment:** Each script initiates a connection to Discord's API to enable interaction with servers and users.
2. **Configuration Loading:** Configuration files, such as tokens and profile data, are loaded to customize the behavior and appearance of the honeypot accounts.
3. **Profile Customization:** Honeypot accounts dynamically change their profile elements, including username, nickname, avatar, bio, and status, to emulate genuine user activity.
4. **DM Monitoring:** The scripts continuously monitor DM activity, capturing relevant information such as sender details, message contents, and timestamps.
5. **Logging:** Detected DMs and relevant information are logged into designated log files for further analysis and review.

### Structure:

1. **Initialization:** The script begins by establishing connections and loading necessary configurations.
2. **Profile Setup:** Initial profile customization, including setting usernames, avatars, and statuses, is performed to ensure variability and authenticity.
3. **Asynchronous Tasks:** Async tasks are created to handle profile updates and status changes at randomized intervals, mimicking natural user behavior.
4. **Message Handling:** The script includes event handlers to intercept and process incoming DMs, extracting relevant information and logging them accordingly.
5. **Logging and Reporting:** Captured DMs are logged into designated log files while also being reported to specified channels for real-time monitoring by moderation teams.

These scripts are essential components of the Discord Honeypot System, working in tandem with the controller script to create a comprehensive monitoring and detection framework. By simulating authentic user interactions while actively monitoring DM activity, these honeypot instances contribute significantly to server security and moderation efforts.

## Credits

- [usernames.txt](https://github.com/jeanphorn/wordlist/blob/master/usernames.txt) - used as the wordlist.txt for the generators.
- [pfps.gg](https://pfps.gg/) - source of all 1000 profile images.

## Warning

This script operates by utilizing methodologies that **are against Discord's Terms of Service (ToS)**, including the use of self-bots. Its creation and distribution are intended for **conceptual and educational purposes only**. Users must be aware of the risks, including potential account bans, and are solely responsible for any consequences arising from its use.

## Disclaimer

This project is a conceptual framework intended for educational and research purposes. The developer disclaims all responsibility for any misuse or violation of Discord's ToS resulting from the deployment of this system. Users are advised to proceed with caution and consider the ethical and legal implications of their actions.

## Support and Contribution

Feedback and contributions are welcome to enhance the system's features and efficiency. Please adhere to standard coding practices and respect Discord's guidelines when proposing changes or additions.
