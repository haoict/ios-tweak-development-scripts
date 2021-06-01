# How to dump header for an ios app

1. Run `iproxy 2222 22`
2. Go to `frida-ios-dump` git directory (which has dump.py) and run `./dump.py com.reddit.Reddit`
3. An IPA file is created. Move it to somewhere like `~/ipa-dump/reddit`. `unzip` it, we can see `Payload/Reddit.app`
4. Go to `ios-tweaks/_scripts/class-dump-helper` and run `./class-dump-helper.py ~/ipa-dump/reddit`