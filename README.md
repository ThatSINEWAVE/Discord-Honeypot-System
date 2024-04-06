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

## Capabilities

The system's honeypot bots are equipped with the following customization abilities to enhance their effectiveness and remain undetectable:

1. **Profile Picture:** Randomly changes from a list of 1,000 curated images.
2. **Username & Nickname:** Randomly changes from a list of 10,000 curated names.
3. **About Me & Pronouns Sections:** Randomly changes from a list of 10,000 curated texts.
4. **Profile Background Color:** Randomly selects from a wide range of color values.
5. **Status Updates:** Switches between online, away, do not disturb, and offline statuses.
6. **Rich Presence:** Simulates activity such as playing a game from a list of 100 curated titles.

## Warning

This script operates by utilizing methodologies that **are against Discord's Terms of Service (ToS)**, including the use of self-bots. Its creation and distribution are intended for **conceptual and educational purposes only**. Users must be aware of the risks, including potential account bans, and are solely responsible for any consequences arising from its use.

## Disclaimer

This project is a conceptual framework intended for educational and research purposes. The developer disclaims all responsibility for any misuse or violation of Discord's ToS resulting from the deployment of this system. Users are advised to proceed with caution and consider the ethical and legal implications of their actions.

## Support and Contribution

Feedback and contributions are welcome to enhance the system's features and efficiency. Please adhere to standard coding practices and respect Discord's guidelines when proposing changes or additions.
