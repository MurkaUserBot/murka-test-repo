#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    MurkaUserBot (telegram userbot)
#    Copyright (C) 2022 SsNiPeR1 5050prop

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import requests


def main():
    port = os.environ.get("PORT", 8080)
    requests.get(f"http://localhost:{port}").raise_for_status()


if __name__ == "__main__":
    main()
