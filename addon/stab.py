import json
import pprint


def register_stab(user_id: str, chat_id) -> str:
    with open('output/stab_list.json', "rb") as stab_list:
        chat_info = json.load(stab_list)

    if str(chat_id) in chat_info.keys():
        if user_id in chat_info[str(chat_id)].keys():
            return "이미 존재하는 유저입니다."

        else:
            chat_info[str(chat_id)][user_id] = {'keyword': [], 'stabbing': 0, 'stabbed': 0}
            try:
                with open('output/stab_list.json', "w", encoding='utf-8') as stab_list:
                    json.dump(chat_info, stab_list, ensure_ascii=False)
            except Exception as e:
                print(e)
                return "유저 등록에 실패했습니다."
            return "유저 등록에 성공했습니다."
    else:
        chat_info[chat_id] = {user_id: {'keyword': [], 'stabbing': 0, 'stabbed': 0}}
        try:
            pprint.pprint(chat_info)
            with open('output/stab_list.json', "w", encoding='utf-8') as stab_list:
                json.dump(chat_info, stab_list, ensure_ascii=False)
        except Exception as e:
            print(e)
            return "유저 등록에 실패했습니다."
        return "유저 등록에 성공했습니다."


def fetch_keyword(chat_id: str, user_id: str, keyword: str):
    with open('output/stab_list.json', "rb") as stab_list:
        chat_info = json.load(stab_list)
    if keyword in chat_info[chat_id][user_id]['keyword']:
        return "이미 존재하는 키워드 입니다."
    chat_info[chat_id][user_id]['keyword'].append(keyword)
    try:
        with open('output/stab_list.json', "w", encoding='utf-8') as stab_list:
            json.dump(chat_info, stab_list, ensure_ascii=False)
    except Exception as e:
        print(e)
        return "키워드 등록에 실패했습니다."
    return f'키워드 등록에 성공했습니다.\n 현재 등록된 키워드: {chat_info[chat_id][user_id]["keyword"]}'


def check_stab_list(user_id: str, chat_id) -> bool:
    with open('output/stab_list.json', "rb") as stab_list:
        chat_info = json.load(stab_list)

    if str(chat_id) in chat_info.keys():
        if user_id in chat_info[str(chat_id)]:
            return True
        else:
            return False
    else:
        return False


def stab(user_id: str, chat_id: str, keyword: str):
    chat_info = None
    with open('output/stab_list.json', "rb") as stab_list:
        chat_info = json.load(stab_list)

    keyword_list: list[str] = []

    for user_list in chat_info[chat_id]:
        print(user_list)
        print(chat_info[chat_id][user_id]['keyword'])
        print(keyword)
        if keyword in chat_info[chat_id][user_list]['keyword']:
            if user_list == user_id:
                return "자살은 안돼요"

            chat_info[chat_id][user_id]['stabbing'] += 1
            chat_info[chat_id][user_list]['stabbed'] += 1

            try:
                with open('output/stab_list.json', "w", encoding='utf-8') as stab_list:
                    json.dump(chat_info, stab_list, ensure_ascii=False)
            except Exception as e:
                print(e)
                return "처리에 실패했습니다."

            return f'{keyword}님을 찔렀습니다.\n데스카운트: {chat_info[chat_id][user_list]["stabbed"]}'
