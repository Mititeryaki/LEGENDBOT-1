from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 25769451
    API_HASH = "7827c57f6d763352104eac8b58d93744"
    # the name to display in your alive message
    ALIVE_NAME = "LegendBoy"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://hwffqxra:LZ0wJmLXRv9rCsgTJf5Cnp-i1lqU2YCl@mahmud.db.elephantsql.com/hwffqxra"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill th this
    LEGEND_STRING = "1AZWarzkBuwowz5K-jlapMGu4ryKFqw0zA6zQJeyIZmh5Tssh3TvQM-kcCyb-sKRLusuxoEqQV0XLQQdkNiJGmU3NDviJGauxsX75_WZODcCM7rQ8nbYHqtSlEmLAHjNoAofxIAKCENwiJw0xK-JW4UWOtqH5Ti_OMA6j2iGvEH0s3WwOoSFfW97nMd_IWZQCPmWt-1nkSyERsc6MBS1s7LNH3aRZFGsSck_mGtgHwZuaiH8tbkcPMkHOyfEjTG58bkB_HQSMzrQSgWRukDBrhoNGMXUNhvkYFdL6QYOAL81P4jvLVZT58R2drlI7oBcp3zrT_C00lO7ZqwyNdm31uLCvccCPYBY="
    # create a new bot in @botfather and fill the following vales with bottoken
    BOT_TOKEN = "5967121399:AAHLD_XwKub0SXhqqB3NSpQTLKTqPM2oDqw"
    # command handler
    HANDLER = "."
    # command hanler for sudo
    SUDO_HANDLER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/LEGEND-AI/PLUGINS"
    EXTERNAL_REPOBRANCH = "main"
    UPSTREAM_REPO = "pro"
    # Your City's TimeZone
    TZ = "Asia/Kolkata"
