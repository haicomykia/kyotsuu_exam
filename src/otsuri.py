"""
令和7年度 大学入学共通テスト 情報1 試作問題
第3問
"""


def maisuu(kingaku: int) -> int:
    """
    枚数（金額）
    :param kingaku:金額
    :return: 枚数が最小となる硬貨枚数
    """
    kouka = (1, 5, 10, 50, 100)
    maisu = 0
    nokori = kingaku
    for yen in reversed(kouka):
        maisu = maisu + nokori // yen
        nokori = nokori % yen
    return maisu


def calc_exchanged_min_number_of_coin(kakaku: int) -> None:
    """
    最小交換硬貨枚数を求める
    :param kakaku:価格
    :return:最小交換硬貨枚数
    """
    min_maisu = 100
    for tsuri in range(0, 99):
        shiharai = kakaku + tsuri
        numbers = maisuu(shiharai) + maisuu(tsuri)
        if numbers < min_maisu:
            min_maisu = numbers
    return min_maisu


if __name__ == '__main__':
    assert calc_exchanged_min_number_of_coin(1) == 1
