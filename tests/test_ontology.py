from arago.ontology import QName


def test_qname():
    name = QName('ogit:yearOfBirth')
    assert name.constant == 'OGIT_YEAR_OF_BIRTH'
    name = QName('ogit.Accounting:TrialBalanceTargetAccountByNumber')
    assert name.constant == 'OGIT_ACCOUNTING_TRIAL_BALANCE_TARGET_ACCOUNT_BY_NUMBER'
    name = QName('ogit.Health.Diagnostics:appID')
    assert name.constant == 'OGIT_HEALTH_DIAGNOSTICS_APP_ID'
