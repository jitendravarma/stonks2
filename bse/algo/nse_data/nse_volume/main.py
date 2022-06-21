import requests

cookies = {
    'NSE-TEST-1': '1910513674.20480.0000',
    'bm_mi': '840F1540E73DB3EC4DB1180BAFCA49DA~2M7075nh1L9e8jhbIlxicw8GhE9GVdPWr3FIcqnYO4PxoppFN43B0q5c1WUy1dDDKFRSHfTt2VW9QlBzCLwFz0mg0zd0jLd332OSeURO0Fx2YPwKk96wvWMZ7JZ5SmD21p+DtQ+NTHvFB3le7ZVMR/im+JlDFlAOAbqOk7Vo+BB0Agubr5h5IU67qZ4FrIF6L+cgPUZY9Co2a0vhNni+kYkkJOvVH9gZ6Ou5CfyvP0Z5cxYEMZdk78FGVsi0HGjnIlaPXxU9uotHyfLzwsiB+FEoea81XZaGFf0JpM6rBtVoi0DTG8jnjFxL+IWL8OkM',
    'bm_sv': '577F823AFBEA3FACA7CB64579AFA2E2C~1u7FKmdHwxej0Sj2+mmGrgkXK4VboNnzgZT5LlFDUYBN/ZzkMWAyBrNYXUnb9KGsMIPtgyNlL3Y7GEmsS7d/CU/taAiw/ZOnGcd65+gTs0GB9X5zb0q6gz4NMtWh6lcajoRAlNj4V304YKpJH4oVofL1BT1hLMHBQaTpwoyIuxg=',
    'ak_bmsc': '1BD3544B4D2F7226DA4DA7C2307CACBC~000000000000000000000000000000~YAAQtP7UF2d/5AKAAQAAO4+IHg8uUACu0/0k/MRTuEgsf/sReRoqElVs8N+KnQ+FzFOOkrUZgBuMGAS5jnrt9pN/inM/Iyb7lLK9tqpeQtx39GXyoNp2CUprmZVhXZ9gP2JImE9QHhH9zyBbk0iBGkjti9to8ZyYzbU5DUpbUqqmn6DkjS+fw2ij1wts8z1pxRqtzWzwpzdNlIQotEyAWUG8sLc/q0xdZ1aYmP6eHwUgqHPYyKks3QWe8z23ILQnlvweGdOOoo7t/jF3YSgQQNOV27iEDKpUFO7iycXeBpVOObIQs1Xx8RtaG6kHvtVXsqR11+0rlaZuG8g85K2UbXTk0GM3KBa3IZXlgbdqEHgS1zShC3k75cbW5HejoKBuwywFWHUbeZrCHcQO+WvYimMNtumnUgk7xueCeksb4J/G9gl7nKLjlu7v2R331AvwEowRPGJr85/V+I/CogpXKLXLPtMxcrylMAyAjB8UVmJIFRcQ',
}

headers = {
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-GPC': '1',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www1.nseindia.com/products/content/equities/indices/historical_index_data.htm',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'NSE-TEST-1=1910513674.20480.0000; bm_mi=840F1540E73DB3EC4DB1180BAFCA49DA~2M7075nh1L9e8jhbIlxicw8GhE9GVdPWr3FIcqnYO4PxoppFN43B0q5c1WUy1dDDKFRSHfTt2VW9QlBzCLwFz0mg0zd0jLd332OSeURO0Fx2YPwKk96wvWMZ7JZ5SmD21p+DtQ+NTHvFB3le7ZVMR/im+JlDFlAOAbqOk7Vo+BB0Agubr5h5IU67qZ4FrIF6L+cgPUZY9Co2a0vhNni+kYkkJOvVH9gZ6Ou5CfyvP0Z5cxYEMZdk78FGVsi0HGjnIlaPXxU9uotHyfLzwsiB+FEoea81XZaGFf0JpM6rBtVoi0DTG8jnjFxL+IWL8OkM; bm_sv=577F823AFBEA3FACA7CB64579AFA2E2C~1u7FKmdHwxej0Sj2+mmGrgkXK4VboNnzgZT5LlFDUYBN/ZzkMWAyBrNYXUnb9KGsMIPtgyNlL3Y7GEmsS7d/CU/taAiw/ZOnGcd65+gTs0GB9X5zb0q6gz4NMtWh6lcajoRAlNj4V304YKpJH4oVofL1BT1hLMHBQaTpwoyIuxg=; ak_bmsc=1BD3544B4D2F7226DA4DA7C2307CACBC~000000000000000000000000000000~YAAQtP7UF2d/5AKAAQAAO4+IHg8uUACu0/0k/MRTuEgsf/sReRoqElVs8N+KnQ+FzFOOkrUZgBuMGAS5jnrt9pN/inM/Iyb7lLK9tqpeQtx39GXyoNp2CUprmZVhXZ9gP2JImE9QHhH9zyBbk0iBGkjti9to8ZyYzbU5DUpbUqqmn6DkjS+fw2ij1wts8z1pxRqtzWzwpzdNlIQotEyAWUG8sLc/q0xdZ1aYmP6eHwUgqHPYyKks3QWe8z23ILQnlvweGdOOoo7t/jF3YSgQQNOV27iEDKpUFO7iycXeBpVOObIQs1Xx8RtaG6kHvtVXsqR11+0rlaZuG8g85K2UbXTk0GM3KBa3IZXlgbdqEHgS1zShC3k75cbW5HejoKBuwywFWHUbeZrCHcQO+WvYimMNtumnUgk7xueCeksb4J/G9gl7nKLjlu7v2R331AvwEowRPGJr85/V+I/CogpXKLXLPtMxcrylMAyAjB8UVmJIFRcQ',
}

params = {
    'indexType': 'NIFTY 50',
    'fromDate': '04-04-2022',
    'toDate': '12-04-2022',
}

response = requests.get('https://www1.nseindia.com/products/dynaContent/equities/indices/historicalindices.jsp',
                        headers=headers, params=params, cookies=cookies)
