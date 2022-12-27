from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 17881150
    API_HASH = "83e83a14784a5355838dd0c24529d52a"
    # the name to display in your alive message
    ALIVE_NAME = "LegendBoy"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://oxkxqagp:846JSW5Jb4sbPZNlowgqkS_HYfWOFyoa@snuffleupagus.db.elephantsql.com/oxkxqagp"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill th this
    LEGEND_STRING = "1AZWarzUBuxvy7WfsPwYssPg2r4fZI2qOFTAGfCO4p1yVN-qK77_xnrlBJg9vse3vLGhOBtPYlvJDSn5sW-3Uml2C2fEeM1XJXsL5k2jHc50aPHpgvDr5J2gdlPCH32HNoQnWOrYaX_pymBc0oTLmVcagwUmkWEdt1gyGyvCt75k_vJw3un_TFZBjWlJgKUKsRvTXkImcZY0rDgFXijl7wjO3Ict9EH5H6zHl69U3m3pPwmzk6yldfbUTcPQk_5Iv6lv6rOWy3xussxP0KimTmYjH5ELUDTvjJ_Pjw9pq8NsFwoG8hvXPsyOGqqjZQuR5UcOkIUead2NoX2hqpwWxoIThVs9uVPE="
    # create a new bot in @botfather and fill the following vales with bottoken
    BOT_TOKEN = "5540365226:AAGaOTQYFSEhGqhRx0cFev6heCDI1JZqsCo"
    # command handler
    HANDLER = "."
    # command hanler for sudo
    SUDO_HANDLER = "."
    # External plugins repo
    EXTRA_REPO = "https://github.com/ITS-LEGENDBOT/PLUGINS"
    EXTRA_REPOBRANCH = "main"
    UPSTREAM_REPO = "pro"
    # Your City's TimeZone
    TZ = "Asia/Kolkata"
