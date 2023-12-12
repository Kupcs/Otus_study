
def test_answer(fix_url, fix_status):
    """pytest tests_for_api/test_module.py --url=https://ya.ru --status_code=200"""
    if fix_url == "https://ya.ru":
        assert fix_status == 200
    else:
        assert fix_status == '404'




