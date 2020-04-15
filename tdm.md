


### auth_group () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 2 | name | b'varchar(80)' | NO | bytearray(b'') |



### auth_group_permissions () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | group_id | b'int(11)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 3 | permission_id | b'int(11)' | NO | bytearray(b'') |



### auth_permission () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | codename | b'varchar(100)' | NO | bytearray(b'') |
| 3 | content_type_id | b'int(11)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 2 | name | b'varchar(255)' | NO | bytearray(b'') |



### auth_user () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 11 | date_joined | b'datetime(6)' | NO | bytearray(b'') |
| 8 | email | b'varchar(254)' | NO | bytearray(b'') |
| 6 | first_name | b'varchar(30)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 10 | is_active | b'tinyint(1)' | NO | bytearray(b'') |
| 9 | is_staff | b'tinyint(1)' | NO | bytearray(b'') |
| 4 | is_superuser | b'tinyint(1)' | NO | bytearray(b'') |
| 3 | last_login | b'datetime(6)' | YES | bytearray(b'') |
| 7 | last_name | b'varchar(150)' | NO | bytearray(b'') |
| 2 | password | b'varchar(128)' | NO | bytearray(b'') |
| 5 | username | b'varchar(150)' | NO | bytearray(b'') |



### auth_user_groups () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | group_id | b'int(11)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 2 | user_id | b'int(11)' | NO | bytearray(b'') |



### auth_user_user_permissions () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 3 | permission_id | b'int(11)' | NO | bytearray(b'') |
| 2 | user_id | b'int(11)' | NO | bytearray(b'') |



### bs_a () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | enddate | b'datetime' | YES | bytearray(b'\xe6\x97\xa5\xe6\x9c\x9f') |
| 1 | indicatorName | b'varchar(50)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe5\x90\x8d\xe7\xa7\xb0') |
| 3 | term | b'decimal(19,4)' | YES | bytearray(b'\xe6\x9c\x9f\xe9\x99\x90') |



### bs_ad () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | footnote_codes | b'varchar(4)' | YES | bytearray(b'') |
| 3 | period | b'varchar(8)' | YES | bytearray(b'') |
| 1 | series_id | b'varchar(255)' | YES | bytearray(b'') |
| 4 | value | b'varchar(20)' | YES | bytearray(b'') |
| 2 | year | b'varchar(8)' | YES | bytearray(b'') |



### bs_com_fut_capital () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | Client_Abbr | b'varchar(50)' | YES | bytearray(b'\xe5\xae\xa2\xe6\x88\xb7\xe5\x90\x8d\xe7\xae\x80\xe7\xa7\xb0') |
| 2 | Client_ID | b'varchar(50)' | YES | bytearray(b'\xe5\xae\xa2\xe6\x88\xb7\xe5\x8f\xb7') |
| 4 | Currency | b'varchar(50)' | YES | bytearray(b'\xe5\xb8\x81\xe7\xa7\x8d') |
| 1 | Date | b'datetime' | YES | bytearray(b'\xe6\x97\xa5\xe6\x9c\x9f') |
| 5 | Field | b'varchar(50)' | YES | bytearray(b'\xe5\xad\x97\xe6\xae\xb5') |
| 6 | Field_CNAME | b'varchar(50)' | YES | bytearray(b'\xe5\xad\x97\xe6\xae\xb5\xe4\xb8\xad\xe6\x96\x87\xe5\x90\xab\xe4\xb9\x89') |
| 8 | isupload | b'varchar(10)' | YES | bytearray(b'\xe6\x98\xaf\xe5\x90\xa6\xe5\xb7\xb2\xe7\xbb\x8f\xe9\x87\x87\xe9\x9b\x86') |
| 7 | value | b'decimal(18,4)' | YES | bytearray(b'\xe5\x80\xbc') |



### bs_employees_mgr () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 3 | manager_id | b'int(11)' | YES | bytearray(b'') |
| 2 | name | b'varchar(100)' | NO | bytearray(b'') |



### bs_fin () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | aid | b'int(5)' | NO | bytearray(b'') |
| 4 | datas | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | date | b'datetime' | YES | bytearray(b'') |
| 1 | ID | b'bigint(20)' | YES | bytearray(b'ID') |



### bs_fin_lc_qfinancialindexnew () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | AccountingStandards | b'int(11)' | YES | bytearray(b'\xe4\xbc\x9a\xe8\xae\xa1\xe5\x87\x86\xe5\x88\x99') |
| 41 | AccountReceivable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe6\x94\xb6\xe8\xb4\xa6\xe6\xac\xbe') |
| 63 | AccountsPayable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe4\xbb\x98\xe8\xb4\xa6\xe6\xac\xbe') |
| 18 | AdministrationExpense | b'decimal(19,4)' | YES | bytearray(b'\xe7\xae\xa1\xe7\x90\x86\xe8\xb4\xb9\xe7\x94\xa8') |
| 20 | AdministrationExpenseRate | b'decimal(19,4)' | YES | bytearray(b'\xe7\xae\xa1\xe7\x90\x86\xe8\xb4\xb9\xe7\x94\xa8\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5\xe6\xaf\x94\xe7\x8e\x87') |
| 19 | AdministrationExpenseYOY | b'decimal(19,4)' | YES | bytearray(b'\xe7\xae\xa1\xe7\x90\x86\xe8\xb4\xb9\xe7\x94\xa8(YOY)') |
| 43 | AdvancePayment | b'decimal(19,4)' | YES | bytearray(b'\xe9\xa2\x84\xe4\xbb\x98\xe6\xac\xbe\xe9\xa1\xb9') |
| 42 | AdvanceReceipts | b'decimal(19,4)' | YES | bytearray(b'\xe9\xa2\x84\xe6\x94\xb6\xe6\xac\xbe\xe9\xa1\xb9') |
| 79 | APDays | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe4\xbb\x98\xe5\xa4\xa9\xe6\x95\xb0\xef\xbc\x88\xe5\xad\xa3\xe5\xba\xa6\xef\xbc\x89') |
| 77 | ARDays | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe6\x94\xb6\xe5\xa4\xa9\xe6\x95\xb0') |
| 24 | AssetImpairmentLoss | b'decimal(19,4)' | YES | bytearray(b'\xe8\xb5\x84\xe4\xba\xa7\xe5\x87\x8f\xe5\x80\xbc\xe6\x8d\x9f\xe5\xa4\xb1') |
| 40 | BillReceivable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe6\x94\xb6\xe7\xa5\xa8\xe6\x8d\xae') |
| 72 | BondsPayable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe4\xbb\x98\xe5\x80\xba\xe5\x88\xb8') |
| 101 | BorrowingRepayment | b'decimal(19,4)' | YES | bytearray(b'\xe5\x81\xbf\xe8\xbf\x98\xe5\x80\xba\xe5\x8a\xa1\xe6\x94\xaf\xe4\xbb\x98\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 3 | BulletinType | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x91\x8a\xe7\xb1\xbb\xe5\x9e\x8b') |
| 88 | CapEx | b'decimal(19,4)' | YES | bytearray(b'\xe8\xb5\x84\xe6\x9c\xac\xe6\x94\xaf\xe5\x87\xba') |
| 80 | CashDays | b'decimal(19,4)' | YES | bytearray(b'\xe7\x8e\xb0\xe9\x87\x91\xe5\x91\xa8\xe6\x9c\x9f') |
| 38 | CashEquivalents | b'decimal(19,4)' | YES | bytearray(b'\xe8\xb4\xa7\xe5\xb8\x81\xe8\xb5\x84\xe9\x87\x91') |
| 98 | CashFromBondsIssue | b'decimal(19,4)' | YES | bytearray(b'\xe5\x8f\x91\xe8\xa1\x8c\xe5\x80\xba\xe5\x88\xb8\xe6\x94\xb6\xe5\x88\xb0\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 97 | CashFromBorrowing | b'decimal(19,4)' | YES | bytearray(b'\xe5\x8f\x96\xe5\xbe\x97\xe5\x80\x9f\xe6\xac\xbe\xe6\x94\xb6\xe5\x88\xb0\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 103 | CashFromInvest | b'decimal(19,4)' | YES | bytearray(b'\xe5\x90\xb8\xe6\x94\xb6\xe6\x8a\x95\xe8\xb5\x84\xe6\x94\xb6\xe5\x88\xb0\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 104 | CashFromMinoSInvestSub | b'decimal(19,4)' | YES | bytearray(b'\xe5\x85\xb6\xe4\xb8\xad:\xe5\xad\x90\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\xb8\xe6\x94\xb6\xe5\xb0\x91\xe6\x95\xb0\xe8\x82\xa1\xe4\xb8\x9c\xe6\x8a\x95\xe8\xb5\x84\xe6\x94\xb6\xe5\x88\xb0\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 92 | CashSale | b'decimal(19,4)' | YES | bytearray(b'\xe7\x8e\xb0\xe9\x87\x91\xe6\x94\xb6\xe5\x85\xa5\xe7\x8e\x87') |
| 94 | CFO2NI | b'decimal(19,4)' | YES | bytearray(b'\xe7\xbb\x8f\xe8\x90\xa5\xe6\xb4\xbb\xe5\x8a\xa8\xe7\x8e\xb0\xe9\x87\x91\xe6\xb5\x81\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6') |
| 95 | CFO2OP | b'decimal(19,4)' | YES | bytearray(b'\xe7\xbb\x8f\xe8\x90\xa5\xe6\xb4\xbb\xe5\x8a\xa8\xe7\x8e\xb0\xe9\x87\x91\xe6\xb5\x81\xe8\x90\xa5\xe4\xb8\x9a\xe5\x88\xa9\xe6\xb6\xa6') |
| 4 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 50 | ConstruInProcess | b'decimal(19,4)' | YES | bytearray(b'\xe5\x9c\xa8\xe5\xbb\xba\xe5\xb7\xa5\xe7\xa8\x8b') |
| 84 | Debt2Equity | b'decimal(19,4)' | YES | bytearray(b'\xe5\x80\xba\xe5\x8a\xa1\xe6\x9d\x83\xe7\x9b\x8a\xe6\xaf\x94\xef\xbc\x88\xe6\x80\xbb\xe5\x80\xba\xe5\x8a\xa1/\xe6\x80\xbb\xe6\x9d\x83\xe7\x9b\x8a\xef\xbc\x89') |
| 96 | DebtFinance | b'decimal(19,4)' | YES | bytearray(b'\xe5\x80\xba\xe5\x8a\xa1\xe8\x9e\x8d\xe8\xb5\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 55 | DeferredTaxAssets | b'decimal(19,4)' | YES | bytearray(b'\xe9\x80\x92\xe5\xbb\xb6\xe6\x89\x80\xe5\xbe\x97\xe7\xa8\x8e\xe8\xb5\x84\xe4\xba\xa7') |
| 52 | DevelopmentExpenditure | b'decimal(19,4)' | YES | bytearray(b'\xe5\xbc\x80\xe5\x8f\x91\xe6\x94\xaf\xe5\x87\xba') |
| 99 | DividendInterestPayment | b'decimal(19,4)' | YES | bytearray(b'\xe5\x88\x86\xe9\x85\x8d\xe8\x82\xa1\xe5\x88\xa9\xe3\x80\x81\xe5\x88\xa9\xe6\xb6\xa6\xe6\x88\x96\xe5\x81\xbf\xe4\xbb\x98\xe5\x88\xa9\xe6\x81\xaf\xe6\x94\xaf\xe4\xbb\x98\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 65 | DividendPayable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe4\xbb\x98\xe8\x82\xa1\xe5\x88\xa9') |
| 33 | EffectiveTaxRate | b'decimal(19,4)' | YES | bytearray(b'\xe6\x9c\x89\xe6\x95\x88\xe6\x89\x80\xe5\xbe\x97\xe7\xa8\x8e\xe7\x8e\x87') |
| 5 | EndDate | b'datetime' | YES | bytearray(b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f') |
| 102 | EquityFinance | b'decimal(19,4)' | YES | bytearray(b'\xe8\x82\xa1\xe6\x9d\x83\xe8\x9e\x8d\xe8\xb5\x84\xe7\x8e\xb0\xe9\x87\x91\xe6\xb5\x81') |
| 81 | FATurnover | b'decimal(19,4)' | YES | bytearray(b'\xe5\x9b\xba\xe5\xae\x9a\xe8\xb5\x84\xe4\xba\xa7\xe5\x91\xa8\xe8\xbd\xac\xe7\x8e\x87\xef\xbc\x88\xe5\xb9\xb4\xe5\x8c\x96\xef\xbc\x89') |
| 91 | FCF | b'decimal(19,4)' | YES | bytearray(b'\xe8\x87\xaa\xe7\x94\xb1\xe7\x8e\xb0\xe9\x87\x91\xe6\xb5\x81') |
| 28 | FinancialExpense | b'decimal(19,4)' | YES | bytearray(b'\xe8\xb4\xa2\xe5\x8a\xa1\xe8\xb4\xb9\xe7\x94\xa8') |
| 49 | FixedAssets | b'decimal(19,4)' | YES | bytearray(b'\xe5\x9b\xba\xe5\xae\x9a\xe8\xb5\x84\xe4\xba\xa7') |
| 89 | FixIntanOtherAssetAcquiCash | b'decimal(19,4)' | YES | bytearray(b'\xe8\xb4\xad\xe5\xbb\xba\xe5\x9b\xba\xe5\xae\x9a\xe8\xb5\x84\xe4\xba\xa7\xe3\x80\x81\xe6\x97\xa0\xe5\xbd\xa2\xe8\xb5\x84\xe4\xba\xa7\xe5\x92\x8c\xe5\x85\xb6\xe4\xbb\x96\xe9\x95\xbf\xe6\x9c\x9f\xe8\xb5\x84\xe4\xba\xa7\xe6\x94\xaf\xe4\xbb\x98\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 90 | FixIntanOtherAssetDispoCash | b'decimal(19,4)' | YES | bytearray(b'\xe5\xa4\x84\xe7\xbd\xae\xe5\x9b\xba\xe5\xae\x9a\xe8\xb5\x84\xe4\xba\xa7\xe3\x80\x81\xe6\x97\xa0\xe5\xbd\xa2\xe8\xb5\x84\xe4\xba\xa7\xe5\x92\x8c\xe5\x85\xb6\xe4\xbb\x96\xe9\x95\xbf\xe6\x9c\x9f\xe8\xb5\x84\xe4\xba\xa7\xe6\x94\xb6\xe5\x9b\x9e\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91\xe5\x87\x80\xe9\xa2\x9d') |
| 93 | GoodsSaleServiceRenderCash | b'decimal(19,4)' | YES | bytearray(b'\xe9\x94\x80\xe5\x94\xae\xe5\x95\x86\xe5\x93\x81\xe3\x80\x81\xe6\x8f\x90\xe4\xbe\x9b\xe5\x8a\xb3\xe5\x8a\xa1\xe6\x94\xb6\xe5\x88\xb0\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 53 | GoodWill | b'decimal(19,4)' | YES | bytearray(b'\xe5\x95\x86\xe8\xaa\x89') |
| 12 | GrossIncomeRatio | b'decimal(19,4)' | YES | bytearray(b'\xe6\xaf\x9b\xe5\x88\xa9\xe7\x8e\x87') |
| 1 | ID | b'bigint(20)' | YES | bytearray(b'ID') |
| 32 | IncomeTaxCost | b'decimal(19,4)' | YES | bytearray(b'\xe5\x87\x8f:\xe6\x89\x80\xe5\xbe\x97\xe7\xa8\x8e\xe8\xb4\xb9\xe7\x94\xa8') |
| 2 | InfoPublDate | b'datetime' | YES | bytearray(b'\xe4\xbf\xa1\xe6\x81\xaf\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f') |
| 105 | inserttime | b'datetime' | YES | bytearray(b'\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4') |
| 51 | IntangibleAssets | b'decimal(19,4)' | YES | bytearray(b'\xe6\x97\xa0\xe5\xbd\xa2\xe8\xb5\x84\xe4\xba\xa7') |
| 68 | InterestPayable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe4\xbb\x98\xe5\x88\xa9\xe6\x81\xaf') |
| 78 | InvDays | b'decimal(19,4)' | YES | bytearray(b'\xe5\xad\x98\xe8\xb4\xa7\xe5\xa4\xa9\xe6\x95\xb0\xef\xbc\x88\xe4\xb8\x8d\xe5\x90\xab\xe6\xaf\x9b\xe5\x88\xa9\xe6\xb6\xa6\xef\xbc\x89') |
| 45 | Inventories | b'decimal(19,4)' | YES | bytearray(b'\xe5\xad\x98\xe8\xb4\xa7') |
| 29 | InvestIncome | b'decimal(19,4)' | YES | bytearray(b'\xe6\x8a\x95\xe8\xb5\x84\xe5\x87\x80\xe6\x94\xb6\xe7\x9b\x8a') |
| 48 | InvestmentProperty | b'decimal(19,4)' | YES | bytearray(b'\xe6\x8a\x95\xe8\xb5\x84\xe6\x80\xa7\xe6\x88\xbf\xe5\x9c\xb0\xe4\xba\xa7') |
| 70 | LoanBondsLongterm | b'decimal(19,4)' | YES | bytearray(b'\xe9\x95\xbf\xe6\x9c\x9f\xe5\x80\x9f\xe6\xac\xbe\xe5\x8f\x8a\xe5\x80\xba\xe5\x88\xb8') |
| 54 | LongDeferredExpense | b'decimal(19,4)' | YES | bytearray(b'\xe9\x95\xbf\xe6\x9c\x9f\xe5\xbe\x85\xe6\x91\x8a\xe8\xb4\xb9\xe7\x94\xa8') |
| 47 | LongtermEquityInvest | b'decimal(19,4)' | YES | bytearray(b'\xe9\x95\xbf\xe6\x9c\x9f\xe8\x82\xa1\xe6\x9d\x83\xe6\x8a\x95\xe8\xb5\x84') |
| 71 | LongtermLoan | b'decimal(19,4)' | YES | bytearray(b'\xe9\x95\xbf\xe6\x9c\x9f\xe5\x80\x9f\xe6\xac\xbe') |
| 6 | Mark | b'int(11)' | YES | bytearray(b'\xe5\x90\x88\xe5\xb9\xb6\xe8\xb0\x83\xe6\x95\xb4\xe6\xa0\x87\xe5\xbf\x97') |
| 87 | NetOperateCashFlow | b'decimal(19,4)' | YES | bytearray(b'\xe7\xbb\x8f\xe8\x90\xa5\xe6\xb4\xbb\xe5\x8a\xa8\xe4\xba\xa7\xe7\x94\x9f\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91\xe6\xb5\x81\xe9\x87\x8f\xe5\x87\x80\xe9\xa2\x9d') |
| 34 | NetProfit | b'decimal(19,4)' | YES | bytearray(b'\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6') |
| 35 | NetProfitRatio | b'decimal(19,4)' | YES | bytearray(b'\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6\xe7\x8e\x87') |
| 37 | NetProfitYOY | b'decimal(19,4)' | YES | bytearray(b'\xe5\x87\x80\xe6\x94\xb6\xe5\x85\xa5(YOY)') |
| 60 | NonCurrentLiabilityIn1Year | b'decimal(19,4)' | YES | bytearray(b'\xe4\xb8\x80\xe5\xb9\xb4\xe5\x86\x85\xe5\x88\xb0\xe6\x9c\x9f\xe7\x9a\x84\xe9\x9d\x9e\xe6\xb5\x81\xe5\x8a\xa8\xe8\xb4\x9f\xe5\x80\xba') |
| 61 | NotAccountsPayable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe4\xbb\x98\xe8\xb4\xa6\xe6\xac\xbe\xe5\x8f\x8a\xe7\xa5\xa8\xe6\x8d\xae') |
| 62 | NotesPayable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe4\xbb\x98\xe7\xa5\xa8\xe6\x8d\xae') |
| 36 | NPParentCompanyOwners | b'decimal(19,4)' | YES | bytearray(b'\xe5\xbd\x92\xe5\xb1\x9e\xe4\xba\x8e\xe6\xaf\x8d\xe5\x85\xac\xe5\x8f\xb8\xe6\x89\x80\xe6\x9c\x89\xe8\x80\x85\xe7\x9a\x84\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6') |
| 10 | OperatingCost | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xaf\xe5\x87\xba') |
| 15 | OperatingExpense | b'decimal(19,4)' | YES | bytearray(b'\xe9\x94\x80\xe5\x94\xae\xe8\xb4\xb9\xe7\x94\xa8') |
| 17 | OperatingExpenseRate | b'decimal(19,4)' | YES | bytearray(b'\xe9\x94\x80\xe5\x94\xae\xe8\xb4\xb9\xe7\x94\xa8\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5\xe6\xaf\x94\xe7\x8e\x87') |
| 16 | OperatingExpenseYOY | b'decimal(19,4)' | YES | bytearray(b'\xe9\x94\x80\xe5\x94\xae\xe8\xb4\xb9\xe7\x94\xa8(YOY)') |
| 11 | OperatingPayoutYOY | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xaf\xe5\x87\xba(YOY)') |
| 25 | OperatingProfit | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe5\x88\xa9\xe6\xb6\xa6') |
| 27 | OperatingProfitMargin | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe5\x88\xa9\xe6\xb6\xa6\xe7\x8e\x87') |
| 26 | OperatingProfitYOY | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe5\x88\xa9\xe6\xb6\xa6(YOY)') |
| 8 | OperatingRevenue | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5') |
| 9 | OperatingRevenueYOY | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5\xe5\x90\x8c\xe6\xaf\x94\xe5\xa2\x9e\xe9\x95\xbf(%)') |
| 13 | OperatingTaxSurcharges | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe7\xa8\x8e\xe9\x87\x91\xe5\x8f\x8a\xe9\x99\x84\xe5\x8a\xa0') |
| 14 | OperatingTaxSurchargesYOY | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe7\xa8\x8e(YOY)') |
| 46 | OtherCurrentAssets | b'decimal(19,4)' | YES | bytearray(b'\xe5\x85\xb6\xe4\xbb\x96\xe6\xb5\x81\xe5\x8a\xa8\xe8\xb5\x84\xe4\xba\xa7') |
| 56 | OtherNonCurrentAssets | b'decimal(19,4)' | YES | bytearray(b'\xe5\x85\xb6\xe4\xbb\x96\xe9\x9d\x9e\xe6\xb5\x81\xe5\x8a\xa8\xe8\xb5\x84\xe4\xba\xa7') |
| 69 | OtherPayable | b'decimal(19,4)' | YES | bytearray(b'\xe5\x85\xb6\xe4\xbb\x96\xe5\xba\x94\xe4\xbb\x98\xe6\xac\xbe') |
| 64 | OtherPayableED | b'decimal(19,4)' | YES | bytearray(b'\xe5\x85\xb6\xe4\xbb\x96\xe5\xba\x94\xe4\xbb\x98\xe6\xac\xbe\xe6\x80\xbb') |
| 44 | OtherReceivableED | b'decimal(19,4)' | YES | bytearray(b'\xe5\x85\xb6\xe4\xbb\x96\xe5\xba\x94\xe6\x94\xb6\xe6\xac\xbe') |
| 100 | ProceedsFromSubToMinoS | b'decimal(19,4)' | YES | bytearray(b'\xe5\x85\xb6\xe4\xb8\xad:\xe5\xad\x90\xe5\x85\xac\xe5\x8f\xb8\xe6\x94\xaf\xe4\xbb\x98\xe7\xbb\x99\xe5\xb0\x91\xe6\x95\xb0\xe8\x82\xa1\xe4\xb8\x9c\xe7\x9a\x84\xe8\x82\xa1\xe5\x88\xa9\xe3\x80\x81\xe5\x88\xa9\xe6\xb6\xa6\xe6\x88\x96\xe5\x81\xbf\xe4\xbb\x98\xe7\x9a\x84\xe5\x88\xa9\xe6\x81\xaf') |
| 76 | Purchase | b'decimal(19,4)' | YES | bytearray(b'\xe9\x87\x87\xe8\xb4\xad') |
| 21 | RAndD | b'decimal(19,4)' | YES | bytearray(b'\xe7\xa0\x94\xe5\x8f\x91\xe8\xb4\xb9\xe7\x94\xa8') |
| 23 | RAndDRate | b'decimal(19,4)' | YES | bytearray(b'\xe7\xa0\x94\xe5\x8f\x91\xe8\xb4\xb9\xe7\x94\xa8\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5\xe6\xaf\x94\xe7\x8e\x87') |
| 22 | RAndDYOY | b'decimal(19,4)' | YES | bytearray(b'\xe7\xa0\x94\xe5\x8f\x91\xe8\xb4\xb9\xe7\x94\xa8(YOY)') |
| 39 | Receivable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe6\x94\xb6') |
| 83 | ROA | b'decimal(19,4)' | YES | bytearray(b'\xe7\xbb\x8f\xe8\x90\xa5\xe6\x80\xa7\xe8\xb5\x84\xe4\xba\xa7\xe5\x9b\x9e\xe6\x8a\xa5\xe7\x8e\x87') |
| 86 | ROE | b'decimal(19,4)' | YES | bytearray(b'\xe5\x87\x80\xe8\xb5\x84\xe4\xba\xa7\xe6\x94\xb6\xe7\x9b\x8a\xe7\x8e\x87') |
| 66 | SalariesPayable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe4\xbb\x98\xe8\x81\x8c\xe5\xb7\xa5\xe8\x96\xaa\xe9\x85\xac') |
| 74 | SEWithoutMI | b'decimal(19,4)' | YES | bytearray(b'\xe5\xbd\x92\xe5\xb1\x9e\xe6\xaf\x8d\xe5\x85\xac\xe5\x8f\xb8\xe8\x82\xa1\xe4\xb8\x9c\xe6\x9d\x83\xe7\x9b\x8a\xe5\x90\x88\xe8\xae\xa1') |
| 58 | ShortTermDebt | b'decimal(19,4)' | YES | bytearray(b'\xe7\x9f\xad\xe6\x9c\x9f\xe6\x9c\x89\xe6\x81\xaf\xe8\xb4\x9f\xe5\x80\xba') |
| 59 | ShortTermLoan | b'decimal(19,4)' | YES | bytearray(b'\xe7\x9f\xad\xe6\x9c\x9f\xe5\x80\x9f\xe6\xac\xbe') |
| 85 | TA2TE | b'decimal(19,4)' | YES | bytearray(b'\xe8\xb5\x84\xe4\xba\xa7\xe6\x9d\x83\xe7\x9b\x8a\xe6\xaf\x94\xef\xbc\x88\xe6\x80\xbb\xe8\xb5\x84\xe4\xba\xa7/\xe6\x80\xbb\xe6\x9d\x83\xe7\x9b\x8a\xef\xbc\x89') |
| 82 | TATurnover | b'decimal(19,4)' | YES | bytearray(b'\xe6\x80\xbb\xe8\xb5\x84\xe4\xba\xa7\xe5\x91\xa8\xe8\xbd\xac\xe7\x8e\x87') |
| 67 | TaxsPayable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe4\xba\xa4\xe7\xa8\x8e\xe8\xb4\xb9') |
| 57 | TotalAssets | b'decimal(19,4)' | YES | bytearray(b'\xe8\xb5\x84\xe4\xba\xa7\xe6\x80\xbb\xe8\xae\xa1') |
| 73 | TotalLiability | b'decimal(19,4)' | YES | bytearray(b'\xe8\xb4\x9f\xe5\x80\xba\xe5\x90\x88\xe8\xae\xa1') |
| 30 | TotalProfit | b'decimal(19,4)' | YES | bytearray(b'\xe5\x88\xa9\xe6\xb6\xa6\xe6\x80\xbb\xe9\xa2\x9d') |
| 31 | TotalProfitYOY | b'decimal(19,4)' | YES | bytearray(b'\xe5\x88\xa9\xe6\xb6\xa6\xe6\x80\xbb\xe9\xa2\x9d(YOY)PBT') |
| 75 | TotalShareholderEquity | b'decimal(19,4)' | YES | bytearray(b'\xe6\x89\x80\xe6\x9c\x89\xe8\x80\x85\xe6\x9d\x83\xe7\x9b\x8a(\xe6\x88\x96\xe8\x82\xa1\xe4\xb8\x9c\xe6\x9d\x83\xe7\x9b\x8a)\xe5\x90\x88\xe8\xae\xa1') |
| 106 | updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### bs_imf_date () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | dbid | b'varchar(50)' | YES | bytearray(b'') |



### bs_join () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 2 | name | b'varchar(100)' | NO | bytearray(b'') |



### bs_join2 () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 2 | name | b'varchar(100)' | NO | bytearray(b'') |



### bs_s1 () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Country | b'varchar(8129)' | NO | bytearray(b'') |



### bs_test () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 17 | bs_description | b'varchar(50)' | YES | bytearray(b'\xe4\xb9\xb0/\xe5\x8d\x96') |
| 9 | exec_comment | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\xb3\xa8\xe9\x87\x8a') |
| 7 | exec_date | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x97\xa5\xe6\x9c\x9f') |
| 10 | exec_exchange | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe4\xba\xa4\xe6\x8d\xa2\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | exec_id | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c(\xe8\xb4\xb8\xe6\x98\x93)\xe6\xa0\x87\xe8\xaf\x86\xe7\xac\xa6\xe3\x80\x82') |
| 1 | exec_original_trade_id | b'varchar(50)' | YES | bytearray(b'\xe5\x8e\x9f\xe5\xa7\x8b\xe6\x89\xa7\xe8\xa1\x8c\xe6\xa0\x87\xe8\xaf\x86\xe7\xac\xa6(\xe6\x95\xb4\xe6\x95\xb0)') |
| 6 | exec_price | b'decimal(18,4)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe4\xbb\xb7\xe6\xa0\xbc') |
| 5 | exec_quantity | b'decimal(18,4)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x95\xb0\xe9\x87\x8f') |
| 11 | exec_quoted_price | b'decimal(18,4)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x8a\xa5\xe4\xbb\xb7') |
| 12 | exec_settlement_date | b'datetime' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbb\x93\xe7\xae\x97\xe6\x97\xa5\xe6\x9c\x9f') |
| 14 | exec_status | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe7\x8a\xb6\xe6\x80\x81') |
| 8 | exec_time | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x97\xb6\xe9\x97\xb4') |
| 13 | exec_trade_reporting_date | b'datetime' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x8a\xa5\xe5\x91\x8a\xe6\x97\xa5\xe6\x9c\x9f') |
| 3 | exec_upd_date | b'datetime' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x9c\x9f') |
| 4 | exec_upd_time | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 44 | inserttime | b'datetime' | YES | bytearray(b'\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4') |
| 27 | ord_accrued_int | b'varchar(50)' | YES | bytearray(b'\xe4\xb8\x8e\xe8\xae\xa2\xe5\x8d\x95\xe6\x9c\x89\xe5\x85\xb3\xe7\x9a\x84\xe5\xba\x94\xe8\xae\xa1\xe5\x88\xa9\xe6\x81\xaf') |
| 21 | ord_blotter | b'varchar(50)' | YES | bytearray(b'\xe8\xae\xa2\xe5\x8d\x95\xe5\x90\xb8\xe5\xa2\xa8\xe7\xba\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 22 | ord_broker | b'varchar(50)' | YES | bytearray(b'\xe7\x9b\xb8\xe5\x85\xb3\xe8\xae\xa2\xe5\x8d\x95\xe4\xbb\xa3\xe7\x90\x86') |
| 26 | ord_commission | b'decimal(18,4)' | YES | bytearray(b'\xe6\x80\xbb\xe8\xae\xa2\xe5\x8d\x95\xe7\x9a\x84\xe4\xbd\xa3\xe9\x87\x91') |
| 24 | ord_currency | b'varchar(50)' | YES | bytearray(b'\xe8\xae\xa2\xe5\x8d\x95\xe7\x9a\x84\xe8\xb4\xa7\xe5\xb8\x81') |
| 18 | ord_exch_id | b'varchar(50)' | YES | bytearray(b'\xe8\xae\xa2\xe5\x8d\x95\xe4\xba\xa4\xe6\x8d\xa2ID') |
| 19 | ord_external_code | b'varchar(50)' | YES | bytearray(b'\xe8\xae\xa2\xe5\x8d\x95\xe5\xa4\x96\xe9\x83\xa8\xe4\xbb\xa3\xe7\xa0\x81') |
| 25 | ord_fee | b'decimal(18,4)' | YES | bytearray(b'\xe6\x80\xbb\xe8\xae\xa2\xe5\x8d\x95\xe8\xb4\xb9\xe7\x94\xa8') |
| 16 | ord_id | b'varchar(50)' | YES | bytearray(b'\xe8\xae\xa2\xe5\x8d\x95ID') |
| 15 | ord_original_order_id | b'varchar(50)' | YES | bytearray(b'\xe5\x8e\x9f\xe5\xa7\x8b\xe8\xae\xa2\xe5\x8d\x95ID') |
| 20 | ord_send_bo | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe9\x80\x81\xe5\x88\xb0\xe5\x90\x8e\xe5\x8f\xb0\xe5\x8a\x9e\xe5\x85\xac\xe5\xae\xa4') |
| 23 | ord_system | b'varchar(50)' | YES | bytearray(b'\xe8\xae\xa2\xe8\xb4\xad\xe7\xb3\xbb\xe7\xbb\x9f') |
| 32 | port_customer | b'varchar(50)' | YES | bytearray(b'\xe6\xb6\x88\xe8\xb4\xb9\xe8\x80\x85') |
| 29 | port_firm_acct_mnem | b'varchar(50)' | YES | bytearray(b'\xe4\xbd\x8d\xe7\xbd\xae\xe5\xb8\x90\xe6\x88\xb7\xe5\x85\xb3\xe8\x81\x94') |
| 28 | port_id | b'varchar(50)' | YES | bytearray(b'\xe6\x8c\x81\xe4\xbb\x93ID') |
| 31 | port_mnem | b'varchar(50)' | YES | bytearray(b'\xe7\xbb\x84') |
| 30 | port_trader | b'varchar(50)' | YES | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe8\x80\x85') |
| 41 | sm_currency | b'varchar(50)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe8\xb4\xa7\xe5\xb8\x81') |
| 37 | sm_cusip | b'varchar(50)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe7\xbb\x9f\xe4\xb8\x80\xe5\xae\x89\xe5\x85\xa8\xe9\x89\xb4\xe5\xae\x9a\xe7\xa8\x8b\xe5\xba\x8f\xe5\xa7\x94\xe5\x91\x98\xe4\xbc\x9aID') |
| 42 | sm_description | b'varchar(300)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe6\x8f\x8f\xe8\xbf\xb0') |
| 35 | sm_dsymbol | b'varchar(50)' | YES | bytearray(b'\xe8\xb1\xa1\xe5\xbe\x81') |
| 39 | sm_ext_sec_code | b'varchar(50)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe5\xa4\x96\xe9\x83\xa8\xe4\xbb\xa3\xe7\xa0\x81') |
| 33 | sm_id | b'varchar(50)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8ID') |
| 36 | sm_isin | b'varchar(50)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe5\x9b\xbd\xe9\x99\x85\xe8\xaf\x81\xe5\x88\xb8\xe8\xaf\x86\xe5\x88\xab\xe7\xbc\x96\xe5\x8f\xb7\xe4\xbd\x93\xe7\xb3\xbbID') |
| 43 | sm_long_security_name | b'varchar(300)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe5\x90\x8d\xe7\xa7\xb0') |
| 40 | sm_sec_type | b'varchar(50)' | YES | bytearray(b'\xe7\xb1\xbb\xe5\x9e\x8b') |
| 38 | sm_sedol | b'varchar(50)' | YES | bytearray(b'Sedol of the security') |
| 34 | sm_symbol | b'varchar(50)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8ID') |
| 45 | updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### bs_test1 () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 17 | bs_description | b'varchar(50)' | YES | bytearray(b'\xe4\xb9\xb0/\xe5\x8d\x96') |
| 9 | exec_comment | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\xb3\xa8\xe9\x87\x8a') |
| 7 | exec_date | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x97\xa5\xe6\x9c\x9f') |
| 10 | exec_exchange | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe4\xba\xa4\xe6\x8d\xa2\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | exec_id | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c(\xe8\xb4\xb8\xe6\x98\x93)\xe6\xa0\x87\xe8\xaf\x86\xe7\xac\xa6\xe3\x80\x82') |
| 1 | exec_original_trade_id | b'varchar(50)' | YES | bytearray(b'\xe5\x8e\x9f\xe5\xa7\x8b\xe6\x89\xa7\xe8\xa1\x8c\xe6\xa0\x87\xe8\xaf\x86\xe7\xac\xa6(\xe6\x95\xb4\xe6\x95\xb0)') |
| 6 | exec_price | b'decimal(18,4)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe4\xbb\xb7\xe6\xa0\xbc') |
| 5 | exec_quantity | b'decimal(18,4)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x95\xb0\xe9\x87\x8f') |
| 11 | exec_quoted_price | b'decimal(18,4)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x8a\xa5\xe4\xbb\xb7') |
| 12 | exec_settlement_date | b'datetime' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbb\x93\xe7\xae\x97\xe6\x97\xa5\xe6\x9c\x9f') |
| 14 | exec_status | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe7\x8a\xb6\xe6\x80\x81') |
| 8 | exec_time | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x97\xb6\xe9\x97\xb4') |
| 13 | exec_trade_reporting_date | b'datetime' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x8a\xa5\xe5\x91\x8a\xe6\x97\xa5\xe6\x9c\x9f') |
| 4 | exec_upd_time | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 44 | inserttime | b'datetime' | YES | bytearray(b'\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4') |
| 3 | max(exec_upd_date) | b'datetime' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x9c\x9f') |
| 27 | ord_accrued_int | b'varchar(50)' | YES | bytearray(b'\xe4\xb8\x8e\xe8\xae\xa2\xe5\x8d\x95\xe6\x9c\x89\xe5\x85\xb3\xe7\x9a\x84\xe5\xba\x94\xe8\xae\xa1\xe5\x88\xa9\xe6\x81\xaf') |
| 21 | ord_blotter | b'varchar(50)' | YES | bytearray(b'\xe8\xae\xa2\xe5\x8d\x95\xe5\x90\xb8\xe5\xa2\xa8\xe7\xba\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 22 | ord_broker | b'varchar(50)' | YES | bytearray(b'\xe7\x9b\xb8\xe5\x85\xb3\xe8\xae\xa2\xe5\x8d\x95\xe4\xbb\xa3\xe7\x90\x86') |
| 26 | ord_commission | b'decimal(18,4)' | YES | bytearray(b'\xe6\x80\xbb\xe8\xae\xa2\xe5\x8d\x95\xe7\x9a\x84\xe4\xbd\xa3\xe9\x87\x91') |
| 24 | ord_currency | b'varchar(50)' | YES | bytearray(b'\xe8\xae\xa2\xe5\x8d\x95\xe7\x9a\x84\xe8\xb4\xa7\xe5\xb8\x81') |
| 18 | ord_exch_id | b'varchar(50)' | YES | bytearray(b'\xe8\xae\xa2\xe5\x8d\x95\xe4\xba\xa4\xe6\x8d\xa2ID') |
| 19 | ord_external_code | b'varchar(50)' | YES | bytearray(b'\xe8\xae\xa2\xe5\x8d\x95\xe5\xa4\x96\xe9\x83\xa8\xe4\xbb\xa3\xe7\xa0\x81') |
| 25 | ord_fee | b'decimal(18,4)' | YES | bytearray(b'\xe6\x80\xbb\xe8\xae\xa2\xe5\x8d\x95\xe8\xb4\xb9\xe7\x94\xa8') |
| 16 | ord_id | b'varchar(50)' | YES | bytearray(b'\xe8\xae\xa2\xe5\x8d\x95ID') |
| 15 | ord_original_order_id | b'varchar(50)' | YES | bytearray(b'\xe5\x8e\x9f\xe5\xa7\x8b\xe8\xae\xa2\xe5\x8d\x95ID') |
| 20 | ord_send_bo | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe9\x80\x81\xe5\x88\xb0\xe5\x90\x8e\xe5\x8f\xb0\xe5\x8a\x9e\xe5\x85\xac\xe5\xae\xa4') |
| 23 | ord_system | b'varchar(50)' | YES | bytearray(b'\xe8\xae\xa2\xe8\xb4\xad\xe7\xb3\xbb\xe7\xbb\x9f') |
| 32 | port_customer | b'varchar(50)' | YES | bytearray(b'\xe6\xb6\x88\xe8\xb4\xb9\xe8\x80\x85') |
| 29 | port_firm_acct_mnem | b'varchar(50)' | YES | bytearray(b'\xe4\xbd\x8d\xe7\xbd\xae\xe5\xb8\x90\xe6\x88\xb7\xe5\x85\xb3\xe8\x81\x94') |
| 28 | port_id | b'varchar(50)' | YES | bytearray(b'\xe6\x8c\x81\xe4\xbb\x93ID') |
| 31 | port_mnem | b'varchar(50)' | YES | bytearray(b'\xe7\xbb\x84') |
| 30 | port_trader | b'varchar(50)' | YES | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe8\x80\x85') |
| 41 | sm_currency | b'varchar(50)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe8\xb4\xa7\xe5\xb8\x81') |
| 37 | sm_cusip | b'varchar(50)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe7\xbb\x9f\xe4\xb8\x80\xe5\xae\x89\xe5\x85\xa8\xe9\x89\xb4\xe5\xae\x9a\xe7\xa8\x8b\xe5\xba\x8f\xe5\xa7\x94\xe5\x91\x98\xe4\xbc\x9aID') |
| 42 | sm_description | b'varchar(300)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe6\x8f\x8f\xe8\xbf\xb0') |
| 35 | sm_dsymbol | b'varchar(50)' | YES | bytearray(b'\xe8\xb1\xa1\xe5\xbe\x81') |
| 39 | sm_ext_sec_code | b'varchar(50)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe5\xa4\x96\xe9\x83\xa8\xe4\xbb\xa3\xe7\xa0\x81') |
| 33 | sm_id | b'varchar(50)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8ID') |
| 36 | sm_isin | b'varchar(50)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe5\x9b\xbd\xe9\x99\x85\xe8\xaf\x81\xe5\x88\xb8\xe8\xaf\x86\xe5\x88\xab\xe7\xbc\x96\xe5\x8f\xb7\xe4\xbd\x93\xe7\xb3\xbbID') |
| 43 | sm_long_security_name | b'varchar(300)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe5\x90\x8d\xe7\xa7\xb0') |
| 40 | sm_sec_type | b'varchar(50)' | YES | bytearray(b'\xe7\xb1\xbb\xe5\x9e\x8b') |
| 38 | sm_sedol | b'varchar(50)' | YES | bytearray(b'Sedol of the security') |
| 34 | sm_symbol | b'varchar(50)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8ID') |
| 45 | updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### bs_test3 () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 17 | bs_description | b'varchar(50)' | YES | bytearray(b'\xe4\xb9\xb0/\xe5\x8d\x96') |
| 9 | exec_comment | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\xb3\xa8\xe9\x87\x8a') |
| 7 | exec_date | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x97\xa5\xe6\x9c\x9f') |
| 10 | exec_exchange | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe4\xba\xa4\xe6\x8d\xa2\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | exec_id | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c(\xe8\xb4\xb8\xe6\x98\x93)\xe6\xa0\x87\xe8\xaf\x86\xe7\xac\xa6\xe3\x80\x82') |
| 1 | exec_original_trade_id | b'varchar(50)' | YES | bytearray(b'\xe5\x8e\x9f\xe5\xa7\x8b\xe6\x89\xa7\xe8\xa1\x8c\xe6\xa0\x87\xe8\xaf\x86\xe7\xac\xa6(\xe6\x95\xb4\xe6\x95\xb0)') |
| 6 | exec_price | b'decimal(18,4)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe4\xbb\xb7\xe6\xa0\xbc') |
| 5 | exec_quantity | b'decimal(18,4)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x95\xb0\xe9\x87\x8f') |
| 11 | exec_quoted_price | b'decimal(18,4)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x8a\xa5\xe4\xbb\xb7') |
| 12 | exec_settlement_date | b'datetime' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbb\x93\xe7\xae\x97\xe6\x97\xa5\xe6\x9c\x9f') |
| 14 | exec_status | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe7\x8a\xb6\xe6\x80\x81') |
| 8 | exec_time | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x97\xb6\xe9\x97\xb4') |
| 13 | exec_trade_reporting_date | b'datetime' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x8a\xa5\xe5\x91\x8a\xe6\x97\xa5\xe6\x9c\x9f') |
| 3 | exec_upd_date | b'datetime' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x9c\x9f') |
| 4 | exec_upd_time | b'varchar(50)' | YES | bytearray(b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 44 | inserttime | b'datetime' | YES | bytearray(b'\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4') |
| 27 | ord_accrued_int | b'varchar(50)' | YES | bytearray(b'\xe4\xb8\x8e\xe8\xae\xa2\xe5\x8d\x95\xe6\x9c\x89\xe5\x85\xb3\xe7\x9a\x84\xe5\xba\x94\xe8\xae\xa1\xe5\x88\xa9\xe6\x81\xaf') |
| 21 | ord_blotter | b'varchar(50)' | YES | bytearray(b'\xe8\xae\xa2\xe5\x8d\x95\xe5\x90\xb8\xe5\xa2\xa8\xe7\xba\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 22 | ord_broker | b'varchar(50)' | YES | bytearray(b'\xe7\x9b\xb8\xe5\x85\xb3\xe8\xae\xa2\xe5\x8d\x95\xe4\xbb\xa3\xe7\x90\x86') |
| 26 | ord_commission | b'decimal(18,4)' | YES | bytearray(b'\xe6\x80\xbb\xe8\xae\xa2\xe5\x8d\x95\xe7\x9a\x84\xe4\xbd\xa3\xe9\x87\x91') |
| 24 | ord_currency | b'varchar(50)' | YES | bytearray(b'\xe8\xae\xa2\xe5\x8d\x95\xe7\x9a\x84\xe8\xb4\xa7\xe5\xb8\x81') |
| 18 | ord_exch_id | b'varchar(50)' | YES | bytearray(b'\xe8\xae\xa2\xe5\x8d\x95\xe4\xba\xa4\xe6\x8d\xa2ID') |
| 19 | ord_external_code | b'varchar(50)' | YES | bytearray(b'\xe8\xae\xa2\xe5\x8d\x95\xe5\xa4\x96\xe9\x83\xa8\xe4\xbb\xa3\xe7\xa0\x81') |
| 25 | ord_fee | b'decimal(18,4)' | YES | bytearray(b'\xe6\x80\xbb\xe8\xae\xa2\xe5\x8d\x95\xe8\xb4\xb9\xe7\x94\xa8') |
| 16 | ord_id | b'varchar(50)' | YES | bytearray(b'\xe8\xae\xa2\xe5\x8d\x95ID') |
| 15 | ord_original_order_id | b'varchar(50)' | YES | bytearray(b'\xe5\x8e\x9f\xe5\xa7\x8b\xe8\xae\xa2\xe5\x8d\x95ID') |
| 20 | ord_send_bo | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe9\x80\x81\xe5\x88\xb0\xe5\x90\x8e\xe5\x8f\xb0\xe5\x8a\x9e\xe5\x85\xac\xe5\xae\xa4') |
| 23 | ord_system | b'varchar(50)' | YES | bytearray(b'\xe8\xae\xa2\xe8\xb4\xad\xe7\xb3\xbb\xe7\xbb\x9f') |
| 32 | port_customer | b'varchar(50)' | YES | bytearray(b'\xe6\xb6\x88\xe8\xb4\xb9\xe8\x80\x85') |
| 29 | port_firm_acct_mnem | b'varchar(50)' | YES | bytearray(b'\xe4\xbd\x8d\xe7\xbd\xae\xe5\xb8\x90\xe6\x88\xb7\xe5\x85\xb3\xe8\x81\x94') |
| 28 | port_id | b'varchar(50)' | YES | bytearray(b'\xe6\x8c\x81\xe4\xbb\x93ID') |
| 31 | port_mnem | b'varchar(50)' | YES | bytearray(b'\xe7\xbb\x84') |
| 30 | port_trader | b'varchar(50)' | YES | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe8\x80\x85') |
| 41 | sm_currency | b'varchar(50)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe8\xb4\xa7\xe5\xb8\x81') |
| 37 | sm_cusip | b'varchar(50)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe7\xbb\x9f\xe4\xb8\x80\xe5\xae\x89\xe5\x85\xa8\xe9\x89\xb4\xe5\xae\x9a\xe7\xa8\x8b\xe5\xba\x8f\xe5\xa7\x94\xe5\x91\x98\xe4\xbc\x9aID') |
| 42 | sm_description | b'varchar(300)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe6\x8f\x8f\xe8\xbf\xb0') |
| 35 | sm_dsymbol | b'varchar(50)' | YES | bytearray(b'\xe8\xb1\xa1\xe5\xbe\x81') |
| 39 | sm_ext_sec_code | b'varchar(50)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe5\xa4\x96\xe9\x83\xa8\xe4\xbb\xa3\xe7\xa0\x81') |
| 33 | sm_id | b'varchar(50)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8ID') |
| 36 | sm_isin | b'varchar(50)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe5\x9b\xbd\xe9\x99\x85\xe8\xaf\x81\xe5\x88\xb8\xe8\xaf\x86\xe5\x88\xab\xe7\xbc\x96\xe5\x8f\xb7\xe4\xbd\x93\xe7\xb3\xbbID') |
| 43 | sm_long_security_name | b'varchar(300)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe5\x90\x8d\xe7\xa7\xb0') |
| 40 | sm_sec_type | b'varchar(50)' | YES | bytearray(b'\xe7\xb1\xbb\xe5\x9e\x8b') |
| 38 | sm_sedol | b'varchar(50)' | YES | bytearray(b'Sedol of the security') |
| 34 | sm_symbol | b'varchar(50)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8ID') |
| 45 | updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### bs_testback () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | AccountingStandards | b'int(11)' | YES | bytearray(b'\xe4\xbc\x9a\xe8\xae\xa1\xe5\x87\x86\xe5\x88\x99') |
| 41 | AccountReceivable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe6\x94\xb6\xe8\xb4\xa6\xe6\xac\xbe') |
| 63 | AccountsPayable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe4\xbb\x98\xe8\xb4\xa6\xe6\xac\xbe') |
| 18 | AdministrationExpense | b'decimal(19,4)' | YES | bytearray(b'\xe7\xae\xa1\xe7\x90\x86\xe8\xb4\xb9\xe7\x94\xa8') |
| 20 | AdministrationExpenseRate | b'decimal(19,4)' | YES | bytearray(b'\xe7\xae\xa1\xe7\x90\x86\xe8\xb4\xb9\xe7\x94\xa8\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5\xe6\xaf\x94\xe7\x8e\x87') |
| 19 | AdministrationExpenseYOY | b'decimal(19,4)' | YES | bytearray(b'\xe7\xae\xa1\xe7\x90\x86\xe8\xb4\xb9\xe7\x94\xa8(YOY)') |
| 43 | AdvancePayment | b'decimal(19,4)' | YES | bytearray(b'\xe9\xa2\x84\xe4\xbb\x98\xe6\xac\xbe\xe9\xa1\xb9') |
| 42 | AdvanceReceipts | b'decimal(19,4)' | YES | bytearray(b'\xe9\xa2\x84\xe6\x94\xb6\xe6\xac\xbe\xe9\xa1\xb9') |
| 79 | APDays | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe4\xbb\x98\xe5\xa4\xa9\xe6\x95\xb0\xef\xbc\x88\xe5\xad\xa3\xe5\xba\xa6\xef\xbc\x89') |
| 77 | ARDays | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe6\x94\xb6\xe5\xa4\xa9\xe6\x95\xb0') |
| 24 | AssetImpairmentLoss | b'decimal(19,4)' | YES | bytearray(b'\xe8\xb5\x84\xe4\xba\xa7\xe5\x87\x8f\xe5\x80\xbc\xe6\x8d\x9f\xe5\xa4\xb1') |
| 40 | BillReceivable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe6\x94\xb6\xe7\xa5\xa8\xe6\x8d\xae') |
| 72 | BondsPayable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe4\xbb\x98\xe5\x80\xba\xe5\x88\xb8') |
| 101 | BorrowingRepayment | b'decimal(19,4)' | YES | bytearray(b'\xe5\x81\xbf\xe8\xbf\x98\xe5\x80\xba\xe5\x8a\xa1\xe6\x94\xaf\xe4\xbb\x98\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 3 | BulletinType | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x91\x8a\xe7\xb1\xbb\xe5\x9e\x8b') |
| 88 | CapEx | b'decimal(19,4)' | YES | bytearray(b'\xe8\xb5\x84\xe6\x9c\xac\xe6\x94\xaf\xe5\x87\xba') |
| 80 | CashDays | b'decimal(19,4)' | YES | bytearray(b'\xe7\x8e\xb0\xe9\x87\x91\xe5\x91\xa8\xe6\x9c\x9f') |
| 38 | CashEquivalents | b'decimal(19,4)' | YES | bytearray(b'\xe8\xb4\xa7\xe5\xb8\x81\xe8\xb5\x84\xe9\x87\x91') |
| 98 | CashFromBondsIssue | b'decimal(19,4)' | YES | bytearray(b'\xe5\x8f\x91\xe8\xa1\x8c\xe5\x80\xba\xe5\x88\xb8\xe6\x94\xb6\xe5\x88\xb0\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 97 | CashFromBorrowing | b'decimal(19,4)' | YES | bytearray(b'\xe5\x8f\x96\xe5\xbe\x97\xe5\x80\x9f\xe6\xac\xbe\xe6\x94\xb6\xe5\x88\xb0\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 103 | CashFromInvest | b'decimal(19,4)' | YES | bytearray(b'\xe5\x90\xb8\xe6\x94\xb6\xe6\x8a\x95\xe8\xb5\x84\xe6\x94\xb6\xe5\x88\xb0\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 104 | CashFromMinoSInvestSub | b'decimal(19,4)' | YES | bytearray(b'\xe5\x85\xb6\xe4\xb8\xad:\xe5\xad\x90\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\xb8\xe6\x94\xb6\xe5\xb0\x91\xe6\x95\xb0\xe8\x82\xa1\xe4\xb8\x9c\xe6\x8a\x95\xe8\xb5\x84\xe6\x94\xb6\xe5\x88\xb0\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 92 | CashSale | b'decimal(19,4)' | YES | bytearray(b'\xe7\x8e\xb0\xe9\x87\x91\xe6\x94\xb6\xe5\x85\xa5\xe7\x8e\x87') |
| 94 | CFO2NI | b'decimal(19,4)' | YES | bytearray(b'\xe7\xbb\x8f\xe8\x90\xa5\xe6\xb4\xbb\xe5\x8a\xa8\xe7\x8e\xb0\xe9\x87\x91\xe6\xb5\x81\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6') |
| 95 | CFO2OP | b'decimal(19,4)' | YES | bytearray(b'\xe7\xbb\x8f\xe8\x90\xa5\xe6\xb4\xbb\xe5\x8a\xa8\xe7\x8e\xb0\xe9\x87\x91\xe6\xb5\x81\xe8\x90\xa5\xe4\xb8\x9a\xe5\x88\xa9\xe6\xb6\xa6') |
| 4 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 50 | ConstruInProcess | b'decimal(19,4)' | YES | bytearray(b'\xe5\x9c\xa8\xe5\xbb\xba\xe5\xb7\xa5\xe7\xa8\x8b') |
| 84 | Debt2Equity | b'decimal(19,4)' | YES | bytearray(b'\xe5\x80\xba\xe5\x8a\xa1\xe6\x9d\x83\xe7\x9b\x8a\xe6\xaf\x94\xef\xbc\x88\xe6\x80\xbb\xe5\x80\xba\xe5\x8a\xa1/\xe6\x80\xbb\xe6\x9d\x83\xe7\x9b\x8a\xef\xbc\x89') |
| 96 | DebtFinance | b'decimal(19,4)' | YES | bytearray(b'\xe5\x80\xba\xe5\x8a\xa1\xe8\x9e\x8d\xe8\xb5\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 55 | DeferredTaxAssets | b'decimal(19,4)' | YES | bytearray(b'\xe9\x80\x92\xe5\xbb\xb6\xe6\x89\x80\xe5\xbe\x97\xe7\xa8\x8e\xe8\xb5\x84\xe4\xba\xa7') |
| 52 | DevelopmentExpenditure | b'decimal(19,4)' | YES | bytearray(b'\xe5\xbc\x80\xe5\x8f\x91\xe6\x94\xaf\xe5\x87\xba') |
| 99 | DividendInterestPayment | b'decimal(19,4)' | YES | bytearray(b'\xe5\x88\x86\xe9\x85\x8d\xe8\x82\xa1\xe5\x88\xa9\xe3\x80\x81\xe5\x88\xa9\xe6\xb6\xa6\xe6\x88\x96\xe5\x81\xbf\xe4\xbb\x98\xe5\x88\xa9\xe6\x81\xaf\xe6\x94\xaf\xe4\xbb\x98\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 65 | DividendPayable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe4\xbb\x98\xe8\x82\xa1\xe5\x88\xa9') |
| 33 | EffectiveTaxRate | b'decimal(19,4)' | YES | bytearray(b'\xe6\x9c\x89\xe6\x95\x88\xe6\x89\x80\xe5\xbe\x97\xe7\xa8\x8e\xe7\x8e\x87') |
| 5 | EndDate | b'datetime' | YES | bytearray(b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f') |
| 102 | EquityFinance | b'decimal(19,4)' | YES | bytearray(b'\xe8\x82\xa1\xe6\x9d\x83\xe8\x9e\x8d\xe8\xb5\x84\xe7\x8e\xb0\xe9\x87\x91\xe6\xb5\x81') |
| 81 | FATurnover | b'decimal(19,4)' | YES | bytearray(b'\xe5\x9b\xba\xe5\xae\x9a\xe8\xb5\x84\xe4\xba\xa7\xe5\x91\xa8\xe8\xbd\xac\xe7\x8e\x87\xef\xbc\x88\xe5\xb9\xb4\xe5\x8c\x96\xef\xbc\x89') |
| 91 | FCF | b'decimal(19,4)' | YES | bytearray(b'\xe8\x87\xaa\xe7\x94\xb1\xe7\x8e\xb0\xe9\x87\x91\xe6\xb5\x81') |
| 28 | FinancialExpense | b'decimal(19,4)' | YES | bytearray(b'\xe8\xb4\xa2\xe5\x8a\xa1\xe8\xb4\xb9\xe7\x94\xa8') |
| 49 | FixedAssets | b'decimal(19,4)' | YES | bytearray(b'\xe5\x9b\xba\xe5\xae\x9a\xe8\xb5\x84\xe4\xba\xa7') |
| 89 | FixIntanOtherAssetAcquiCash | b'decimal(19,4)' | YES | bytearray(b'\xe8\xb4\xad\xe5\xbb\xba\xe5\x9b\xba\xe5\xae\x9a\xe8\xb5\x84\xe4\xba\xa7\xe3\x80\x81\xe6\x97\xa0\xe5\xbd\xa2\xe8\xb5\x84\xe4\xba\xa7\xe5\x92\x8c\xe5\x85\xb6\xe4\xbb\x96\xe9\x95\xbf\xe6\x9c\x9f\xe8\xb5\x84\xe4\xba\xa7\xe6\x94\xaf\xe4\xbb\x98\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 90 | FixIntanOtherAssetDispoCash | b'decimal(19,4)' | YES | bytearray(b'\xe5\xa4\x84\xe7\xbd\xae\xe5\x9b\xba\xe5\xae\x9a\xe8\xb5\x84\xe4\xba\xa7\xe3\x80\x81\xe6\x97\xa0\xe5\xbd\xa2\xe8\xb5\x84\xe4\xba\xa7\xe5\x92\x8c\xe5\x85\xb6\xe4\xbb\x96\xe9\x95\xbf\xe6\x9c\x9f\xe8\xb5\x84\xe4\xba\xa7\xe6\x94\xb6\xe5\x9b\x9e\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91\xe5\x87\x80\xe9\xa2\x9d') |
| 93 | GoodsSaleServiceRenderCash | b'decimal(19,4)' | YES | bytearray(b'\xe9\x94\x80\xe5\x94\xae\xe5\x95\x86\xe5\x93\x81\xe3\x80\x81\xe6\x8f\x90\xe4\xbe\x9b\xe5\x8a\xb3\xe5\x8a\xa1\xe6\x94\xb6\xe5\x88\xb0\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 53 | GoodWill | b'decimal(19,4)' | YES | bytearray(b'\xe5\x95\x86\xe8\xaa\x89') |
| 12 | GrossIncomeRatio | b'decimal(19,4)' | YES | bytearray(b'\xe6\xaf\x9b\xe5\x88\xa9\xe7\x8e\x87') |
| 1 | ID | b'bigint(20)' | YES | bytearray(b'ID') |
| 32 | IncomeTaxCost | b'decimal(19,4)' | YES | bytearray(b'\xe5\x87\x8f:\xe6\x89\x80\xe5\xbe\x97\xe7\xa8\x8e\xe8\xb4\xb9\xe7\x94\xa8') |
| 2 | InfoPublDate | b'datetime' | YES | bytearray(b'\xe4\xbf\xa1\xe6\x81\xaf\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f') |
| 105 | inserttime | b'datetime' | YES | bytearray(b'\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4') |
| 51 | IntangibleAssets | b'decimal(19,4)' | YES | bytearray(b'\xe6\x97\xa0\xe5\xbd\xa2\xe8\xb5\x84\xe4\xba\xa7') |
| 68 | InterestPayable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe4\xbb\x98\xe5\x88\xa9\xe6\x81\xaf') |
| 78 | InvDays | b'decimal(19,4)' | YES | bytearray(b'\xe5\xad\x98\xe8\xb4\xa7\xe5\xa4\xa9\xe6\x95\xb0\xef\xbc\x88\xe4\xb8\x8d\xe5\x90\xab\xe6\xaf\x9b\xe5\x88\xa9\xe6\xb6\xa6\xef\xbc\x89') |
| 45 | Inventories | b'decimal(19,4)' | YES | bytearray(b'\xe5\xad\x98\xe8\xb4\xa7') |
| 29 | InvestIncome | b'decimal(19,4)' | YES | bytearray(b'\xe6\x8a\x95\xe8\xb5\x84\xe5\x87\x80\xe6\x94\xb6\xe7\x9b\x8a') |
| 48 | InvestmentProperty | b'decimal(19,4)' | YES | bytearray(b'\xe6\x8a\x95\xe8\xb5\x84\xe6\x80\xa7\xe6\x88\xbf\xe5\x9c\xb0\xe4\xba\xa7') |
| 70 | LoanBondsLongterm | b'decimal(19,4)' | YES | bytearray(b'\xe9\x95\xbf\xe6\x9c\x9f\xe5\x80\x9f\xe6\xac\xbe\xe5\x8f\x8a\xe5\x80\xba\xe5\x88\xb8') |
| 54 | LongDeferredExpense | b'decimal(19,4)' | YES | bytearray(b'\xe9\x95\xbf\xe6\x9c\x9f\xe5\xbe\x85\xe6\x91\x8a\xe8\xb4\xb9\xe7\x94\xa8') |
| 47 | LongtermEquityInvest | b'decimal(19,4)' | YES | bytearray(b'\xe9\x95\xbf\xe6\x9c\x9f\xe8\x82\xa1\xe6\x9d\x83\xe6\x8a\x95\xe8\xb5\x84') |
| 71 | LongtermLoan | b'decimal(19,4)' | YES | bytearray(b'\xe9\x95\xbf\xe6\x9c\x9f\xe5\x80\x9f\xe6\xac\xbe') |
| 6 | Mark | b'int(11)' | YES | bytearray(b'\xe5\x90\x88\xe5\xb9\xb6\xe8\xb0\x83\xe6\x95\xb4\xe6\xa0\x87\xe5\xbf\x97') |
| 87 | NetOperateCashFlow | b'decimal(19,4)' | YES | bytearray(b'\xe7\xbb\x8f\xe8\x90\xa5\xe6\xb4\xbb\xe5\x8a\xa8\xe4\xba\xa7\xe7\x94\x9f\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91\xe6\xb5\x81\xe9\x87\x8f\xe5\x87\x80\xe9\xa2\x9d') |
| 34 | NetProfit | b'decimal(19,4)' | YES | bytearray(b'\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6') |
| 35 | NetProfitRatio | b'decimal(19,4)' | YES | bytearray(b'\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6\xe7\x8e\x87') |
| 37 | NetProfitYOY | b'decimal(19,4)' | YES | bytearray(b'\xe5\x87\x80\xe6\x94\xb6\xe5\x85\xa5(YOY)') |
| 60 | NonCurrentLiabilityIn1Year | b'decimal(19,4)' | YES | bytearray(b'\xe4\xb8\x80\xe5\xb9\xb4\xe5\x86\x85\xe5\x88\xb0\xe6\x9c\x9f\xe7\x9a\x84\xe9\x9d\x9e\xe6\xb5\x81\xe5\x8a\xa8\xe8\xb4\x9f\xe5\x80\xba') |
| 61 | NotAccountsPayable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe4\xbb\x98\xe8\xb4\xa6\xe6\xac\xbe\xe5\x8f\x8a\xe7\xa5\xa8\xe6\x8d\xae') |
| 62 | NotesPayable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe4\xbb\x98\xe7\xa5\xa8\xe6\x8d\xae') |
| 36 | NPParentCompanyOwners | b'decimal(19,4)' | YES | bytearray(b'\xe5\xbd\x92\xe5\xb1\x9e\xe4\xba\x8e\xe6\xaf\x8d\xe5\x85\xac\xe5\x8f\xb8\xe6\x89\x80\xe6\x9c\x89\xe8\x80\x85\xe7\x9a\x84\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6') |
| 10 | OperatingCost | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xaf\xe5\x87\xba') |
| 15 | OperatingExpense | b'decimal(19,4)' | YES | bytearray(b'\xe9\x94\x80\xe5\x94\xae\xe8\xb4\xb9\xe7\x94\xa8') |
| 17 | OperatingExpenseRate | b'decimal(19,4)' | YES | bytearray(b'\xe9\x94\x80\xe5\x94\xae\xe8\xb4\xb9\xe7\x94\xa8\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5\xe6\xaf\x94\xe7\x8e\x87') |
| 16 | OperatingExpenseYOY | b'decimal(19,4)' | YES | bytearray(b'\xe9\x94\x80\xe5\x94\xae\xe8\xb4\xb9\xe7\x94\xa8(YOY)') |
| 11 | OperatingPayoutYOY | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xaf\xe5\x87\xba(YOY)') |
| 25 | OperatingProfit | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe5\x88\xa9\xe6\xb6\xa6') |
| 27 | OperatingProfitMargin | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe5\x88\xa9\xe6\xb6\xa6\xe7\x8e\x87') |
| 26 | OperatingProfitYOY | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe5\x88\xa9\xe6\xb6\xa6(YOY)') |
| 8 | OperatingRevenue | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5') |
| 9 | OperatingRevenueYOY | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5\xe5\x90\x8c\xe6\xaf\x94\xe5\xa2\x9e\xe9\x95\xbf(%)') |
| 13 | OperatingTaxSurcharges | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe7\xa8\x8e\xe9\x87\x91\xe5\x8f\x8a\xe9\x99\x84\xe5\x8a\xa0') |
| 14 | OperatingTaxSurchargesYOY | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe7\xa8\x8e(YOY)') |
| 46 | OtherCurrentAssets | b'decimal(19,4)' | YES | bytearray(b'\xe5\x85\xb6\xe4\xbb\x96\xe6\xb5\x81\xe5\x8a\xa8\xe8\xb5\x84\xe4\xba\xa7') |
| 56 | OtherNonCurrentAssets | b'decimal(19,4)' | YES | bytearray(b'\xe5\x85\xb6\xe4\xbb\x96\xe9\x9d\x9e\xe6\xb5\x81\xe5\x8a\xa8\xe8\xb5\x84\xe4\xba\xa7') |
| 69 | OtherPayable | b'decimal(19,4)' | YES | bytearray(b'\xe5\x85\xb6\xe4\xbb\x96\xe5\xba\x94\xe4\xbb\x98\xe6\xac\xbe') |
| 64 | OtherPayableED | b'decimal(19,4)' | YES | bytearray(b'\xe5\x85\xb6\xe4\xbb\x96\xe5\xba\x94\xe4\xbb\x98\xe6\xac\xbe\xe6\x80\xbb') |
| 44 | OtherReceivableED | b'decimal(19,4)' | YES | bytearray(b'\xe5\x85\xb6\xe4\xbb\x96\xe5\xba\x94\xe6\x94\xb6\xe6\xac\xbe') |
| 100 | ProceedsFromSubToMinoS | b'decimal(19,4)' | YES | bytearray(b'\xe5\x85\xb6\xe4\xb8\xad:\xe5\xad\x90\xe5\x85\xac\xe5\x8f\xb8\xe6\x94\xaf\xe4\xbb\x98\xe7\xbb\x99\xe5\xb0\x91\xe6\x95\xb0\xe8\x82\xa1\xe4\xb8\x9c\xe7\x9a\x84\xe8\x82\xa1\xe5\x88\xa9\xe3\x80\x81\xe5\x88\xa9\xe6\xb6\xa6\xe6\x88\x96\xe5\x81\xbf\xe4\xbb\x98\xe7\x9a\x84\xe5\x88\xa9\xe6\x81\xaf') |
| 76 | Purchase | b'decimal(19,4)' | YES | bytearray(b'\xe9\x87\x87\xe8\xb4\xad') |
| 21 | RAndD | b'decimal(19,4)' | YES | bytearray(b'\xe7\xa0\x94\xe5\x8f\x91\xe8\xb4\xb9\xe7\x94\xa8') |
| 23 | RAndDRate | b'decimal(19,4)' | YES | bytearray(b'\xe7\xa0\x94\xe5\x8f\x91\xe8\xb4\xb9\xe7\x94\xa8\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5\xe6\xaf\x94\xe7\x8e\x87') |
| 22 | RAndDYOY | b'decimal(19,4)' | YES | bytearray(b'\xe7\xa0\x94\xe5\x8f\x91\xe8\xb4\xb9\xe7\x94\xa8(YOY)') |
| 39 | Receivable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe6\x94\xb6') |
| 83 | ROA | b'decimal(19,4)' | YES | bytearray(b'\xe7\xbb\x8f\xe8\x90\xa5\xe6\x80\xa7\xe8\xb5\x84\xe4\xba\xa7\xe5\x9b\x9e\xe6\x8a\xa5\xe7\x8e\x87') |
| 86 | ROE | b'decimal(19,4)' | YES | bytearray(b'\xe5\x87\x80\xe8\xb5\x84\xe4\xba\xa7\xe6\x94\xb6\xe7\x9b\x8a\xe7\x8e\x87') |
| 66 | SalariesPayable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe4\xbb\x98\xe8\x81\x8c\xe5\xb7\xa5\xe8\x96\xaa\xe9\x85\xac') |
| 74 | SEWithoutMI | b'decimal(19,4)' | YES | bytearray(b'\xe5\xbd\x92\xe5\xb1\x9e\xe6\xaf\x8d\xe5\x85\xac\xe5\x8f\xb8\xe8\x82\xa1\xe4\xb8\x9c\xe6\x9d\x83\xe7\x9b\x8a\xe5\x90\x88\xe8\xae\xa1') |
| 58 | ShortTermDebt | b'decimal(19,4)' | YES | bytearray(b'\xe7\x9f\xad\xe6\x9c\x9f\xe6\x9c\x89\xe6\x81\xaf\xe8\xb4\x9f\xe5\x80\xba') |
| 59 | ShortTermLoan | b'decimal(19,4)' | YES | bytearray(b'\xe7\x9f\xad\xe6\x9c\x9f\xe5\x80\x9f\xe6\xac\xbe') |
| 85 | TA2TE | b'decimal(19,4)' | YES | bytearray(b'\xe8\xb5\x84\xe4\xba\xa7\xe6\x9d\x83\xe7\x9b\x8a\xe6\xaf\x94\xef\xbc\x88\xe6\x80\xbb\xe8\xb5\x84\xe4\xba\xa7/\xe6\x80\xbb\xe6\x9d\x83\xe7\x9b\x8a\xef\xbc\x89') |
| 82 | TATurnover | b'decimal(19,4)' | YES | bytearray(b'\xe6\x80\xbb\xe8\xb5\x84\xe4\xba\xa7\xe5\x91\xa8\xe8\xbd\xac\xe7\x8e\x87') |
| 67 | TaxsPayable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe4\xba\xa4\xe7\xa8\x8e\xe8\xb4\xb9') |
| 57 | TotalAssets | b'decimal(19,4)' | YES | bytearray(b'\xe8\xb5\x84\xe4\xba\xa7\xe6\x80\xbb\xe8\xae\xa1') |
| 73 | TotalLiability | b'decimal(19,4)' | YES | bytearray(b'\xe8\xb4\x9f\xe5\x80\xba\xe5\x90\x88\xe8\xae\xa1') |
| 30 | TotalProfit | b'decimal(19,4)' | YES | bytearray(b'\xe5\x88\xa9\xe6\xb6\xa6\xe6\x80\xbb\xe9\xa2\x9d') |
| 31 | TotalProfitYOY | b'decimal(19,4)' | YES | bytearray(b'\xe5\x88\xa9\xe6\xb6\xa6\xe6\x80\xbb\xe9\xa2\x9d(YOY)PBT') |
| 75 | TotalShareholderEquity | b'decimal(19,4)' | YES | bytearray(b'\xe6\x89\x80\xe6\x9c\x89\xe8\x80\x85\xe6\x9d\x83\xe7\x9b\x8a(\xe6\x88\x96\xe8\x82\xa1\xe4\xb8\x9c\xe6\x9d\x83\xe7\x9b\x8a)\xe5\x90\x88\xe8\xae\xa1') |
| 106 | updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### c_ed_macroindicatordata_inc () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | DataValue | b'decimal(28,6)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe6\x8d\xae') |
| 1 | EndDate | b'datetime' | YES | bytearray(b'\xe6\x97\xa5\xe6\x9c\x9f') |
| 2 | IndicatorCode | b'int(11)' | NO | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe5\x86\x85\xe9\x83\xa8\xe7\xbc\x96\xe7\xa0\x81') |



### c_in_indicatordatav_inc () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | DataValue | b'decimal(28,6)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe6\x8d\xae') |
| 1 | EndDate | b'datetime' | YES | bytearray(b'\xe6\x97\xa5\xe6\x9c\x9f') |
| 2 | IndicatorCode | b'int(11)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe5\x86\x85\xe9\x83\xa8\xe7\xbc\x96\xe7\xa0\x81') |



### django_admin_log () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | action_flag | b'smallint(5) unsigned' | NO | bytearray(b'') |
| 2 | action_time | b'datetime(6)' | NO | bytearray(b'') |
| 6 | change_message | b'longtext' | NO | bytearray(b'') |
| 7 | content_type_id | b'int(11)' | YES | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 3 | object_id | b'longtext' | YES | bytearray(b'') |
| 4 | object_repr | b'varchar(200)' | NO | bytearray(b'') |
| 8 | user_id | b'int(11)' | NO | bytearray(b'') |



### django_content_type () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | app_label | b'varchar(100)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 3 | model | b'varchar(100)' | NO | bytearray(b'') |



### django_migrations () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | app | b'varchar(255)' | NO | bytearray(b'') |
| 4 | applied | b'datetime(6)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 3 | name | b'varchar(255)' | NO | bytearray(b'') |



### django_session () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | expire_date | b'datetime(6)' | NO | bytearray(b'') |
| 2 | session_data | b'longtext' | NO | bytearray(b'') |
| 1 | session_key | b'varchar(40)' | NO | bytearray(b'') |



### fin_proprietary_investment_detail_tmp () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | account_name | b'varchar(8)' | NO | bytearray(b'') |
| 3 | account_type | b'varchar(2)' | NO | bytearray(b'') |
| 5 | bank_transfer_fs | b'decimal(18,4)' | YES | bytearray(b'\xe5\x80\xbc') |
| 1 | enddate | b'datetime' | YES | bytearray(b'\xe6\x97\xa5\xe6\x9c\x9f') |
| 2 | startdate | b'datetime' | YES | bytearray(b'\xe6\x97\xa5\xe6\x9c\x9f') |



### fin_proprietary_investment_sum () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | accumulated_income | b'decimal(20,2)' | YES | bytearray(b'\xe7\xb4\xaf\xe8\xae\xa1\xe6\x94\xb6\xe7\x9b\x8a') |
| 7 | annualized_return | b'decimal(20,4)' | YES | bytearray(b'\xe5\xb9\xb4\xe5\x8c\x96\xe6\x94\xb6\xe7\x9b\x8a\xe7\x8e\x87') |
| 6 | capital | b'decimal(20,2)' | YES | bytearray(b'\xe6\x9c\xac\xe9\x87\x91') |
| 1 | enddate | b'date' | YES | bytearray(b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xb6\xe9\x97\xb4') |
| 4 | incometype | b'varchar(50)' | YES | bytearray(b'\xe6\x94\xb6\xe7\x9b\x8a\xe7\xb1\xbb\xe5\x88\xab') |
| 8 | inserttime | b'timestamp' | YES | bytearray(b'\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4') |
| 3 | investmenttype | b'varchar(20)' | YES | bytearray(b'\xe6\x8a\x95\xe8\xb5\x84\xe7\xb1\xbb\xe5\x88\xab') |
| 2 | startdate | b'date' | YES | bytearray(b'\xe8\xb5\xb7\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4') |
| 9 | updatetime | b'timestamp' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### hospital-beds-per-1000-people () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | Code | b'varchar(255)' | YES | bytearray(b'') |
| 1 | Entity | b'varchar(255)' | YES | bytearray(b'') |
| 4 | Hospital beds (per 1,000 people) (per 1,000 people) | b'decimal(20,4)' | YES | bytearray(b'') |
| 3 | Year | b'varchar(255)' | YES | bytearray(b'') |



### hospital-beds-vs-gdp () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | Code | b'varchar(255)' | YES | bytearray(b'') |
| 1 | Entity | b'varchar(255)' | YES | bytearray(b'') |
| 5 | GDP per capita (int.-$) (international-$) | b'decimal(20,4)' | YES | bytearray(b'') |
| 4 | Hospital beds per 1,000 people (per 1,000 people) | b'decimal(20,4)' | YES | bytearray(b'') |
| 3 | Year | b'varchar(255)' | YES | bytearray(b'') |



### imf_database_pgi () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | dbid | b'varchar(50)' | YES | bytearray(b'') |
| 1 | dbname | b'varchar(255)' | YES | bytearray(b'') |
| 3 | freq | b'varchar(10)' | YES | bytearray(b'') |
| 5 | indicatorcode | b'varchar(50)' | YES | bytearray(b'') |
| 9 | obs_value | b'varchar(255)' | YES | bytearray(b'') |
| 4 | ref_area | b'varchar(50)' | YES | bytearray(b'') |
| 7 | time_format | b'varchar(50)' | YES | bytearray(b'') |
| 8 | time_period | b'varchar(50)' | YES | bytearray(b'') |
| 6 | unit_mult | b'varchar(255)' | YES | bytearray(b'') |
| 10 | updatetime | b'datetime' | YES | bytearray(b'') |



### imf_database_pgi2 () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | dbid | b'varchar(50)' | YES | bytearray(b'') |
| 1 | dbname | b'varchar(255)' | YES | bytearray(b'') |
| 3 | freq | b'varchar(10)' | YES | bytearray(b'') |
| 5 | indicatorcode | b'varchar(50)' | YES | bytearray(b'') |
| 9 | obs_value | b'varchar(255)' | YES | bytearray(b'') |
| 4 | ref_area | b'varchar(50)' | YES | bytearray(b'') |
| 7 | time_format | b'varchar(50)' | YES | bytearray(b'') |
| 8 | time_period | b'varchar(50)' | YES | bytearray(b'') |
| 6 | unit_mult | b'varchar(255)' | YES | bytearray(b'') |
| 10 | updatetime | b'datetime' | YES | bytearray(b'') |



### medical-doctors-per-1000-people-vs-gdp-per-capita () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | Code | b'varchar(255)' | YES | bytearray(b'') |
| 1 | Entity | b'varchar(255)' | YES | bytearray(b'') |
| 5 | GDP per capita (int.-$) (international-$) | b'decimal(20,4)' | YES | bytearray(b'') |
| 4 | Medical doctors per 1,000 people (per 1,000 people) | b'decimal(20,4)' | YES | bytearray(b'') |
| 6 | Population, total | b'decimal(20,4)' | YES | bytearray(b'') |
| 3 | Year | b'varchar(255)' | YES | bytearray(b'') |



### mid_balancesheetall_data () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 8 | AccountingStandards | b'int(11)' | NO | bytearray(b'\xe4\xbc\x9a\xe8\xae\xa1\xe5\x87\x86\xe5\x88\x99') |
| 12 | AccountReceivable | b'decimal(19,4)' | YES | bytearray(b'') |
| 33 | AccountsPayable | b'decimal(19,4)' | YES | bytearray(b'') |
| 14 | AdvancePayment | b'decimal(19,4)' | YES | bytearray(b'') |
| 13 | AdvanceReceipts | b'decimal(19,4)' | YES | bytearray(b'') |
| 11 | BillReceivable | b'decimal(19,4)' | YES | bytearray(b'') |
| 41 | BondsPayable | b'decimal(19,4)' | YES | bytearray(b'') |
| 3 | BulletinType | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x91\x8a\xe7\xb1\xbb\xe5\x88\xab') |
| 10 | CashEquivalents | b'decimal(19,4)' | YES | bytearray(b'\xe8\xb4\xa7\xe5\xb8\x81\xe8\xb5\x84\xe9\x87\x91/\xe7\x8e\xb0\xe9\x87\x91\xe5\x8f\x8a\xe5\xad\x98\xe6\x94\xbe\xe4\xb8\xad\xe5\xa4\xae\xe9\x93\xb6\xe8\xa1\x8c\xe6\xac\xbe\xe9\xa1\xb9(\xe5\x85\x83)') |
| 4 | CompanyCode | b'int(11)' | NO | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 21 | ConstruInProcess | b'decimal(19,4)' | YES | bytearray(b'') |
| 26 | DeferredTaxAssets | b'decimal(19,4)' | YES | bytearray(b'') |
| 23 | DevelopmentExpenditure | b'decimal(19,4)' | YES | bytearray(b'') |
| 35 | DividendPayable | b'decimal(19,4)' | YES | bytearray(b'') |
| 5 | EndDate | b'datetime' | NO | bytearray(b'\xe6\x97\xa5\xe6\x9c\x9f') |
| 9 | EnterpriseType | b'int(11)' | NO | bytearray(b'\xe5\xb7\xa5\xe4\xb8\x9a\xe4\xbc\x81\xe4\xb8\x9a\xe7\xb1\xbb\xe5\x9e\x8b') |
| 20 | FixedAssets | b'decimal(19,4)' | YES | bytearray(b'') |
| 24 | GoodWill | b'decimal(19,4)' | YES | bytearray(b'') |
| 1 | ID | b'bigint(20)' | NO | bytearray(b'ID') |
| 6 | IfAdjusted | b'int(11)' | NO | bytearray(b'\xe6\x98\xaf\xe5\x90\xa6\xe8\xb0\x83\xe6\x95\xb4') |
| 7 | IfMerged | b'int(11)' | NO | bytearray(b'\xe5\x90\x88\xe5\xb9\xb6\xe6\xa0\x87\xe5\xbf\x97') |
| 2 | InfoPublDate | b'datetime' | NO | bytearray(b'\xe4\xbf\xa1\xe6\x81\xaf\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f') |
| 22 | IntangibleAssets | b'decimal(19,4)' | YES | bytearray(b'') |
| 38 | InterestPayable | b'decimal(19,4)' | YES | bytearray(b'') |
| 16 | Inventories | b'decimal(19,4)' | YES | bytearray(b'') |
| 19 | InvestmentProperty | b'decimal(19,4)' | YES | bytearray(b'') |
| 25 | LongDeferredExpense | b'decimal(19,4)' | YES | bytearray(b'') |
| 18 | LongtermEquityInvest | b'decimal(19,4)' | YES | bytearray(b'') |
| 40 | LongtermLoan | b'decimal(19,4)' | YES | bytearray(b'') |
| 31 | NonCurrentLiabilityIn1Year | b'decimal(19,4)' | YES | bytearray(b'') |
| 28 | NotAccountsPayable | b'decimal(19,4)' | YES | bytearray(b'') |
| 32 | NotesPayable | b'decimal(19,4)' | YES | bytearray(b'') |
| 17 | OtherCurrentAssets | b'decimal(19,4)' | YES | bytearray(b'') |
| 27 | OtherNonCurrentAssets | b'decimal(19,4)' | YES | bytearray(b'') |
| 39 | OtherPayable | b'decimal(19,4)' | YES | bytearray(b'') |
| 34 | OtherPayableED | b'decimal(19,4)' | YES | bytearray(b'') |
| 15 | OtherReceivableED | b'decimal(19,4)' | YES | bytearray(b'') |
| 36 | SalariesPayable | b'decimal(19,4)' | YES | bytearray(b'') |
| 43 | SEWithoutMI | b'decimal(19,4)' | YES | bytearray(b'') |
| 30 | ShortTermLoan | b'decimal(19,4)' | YES | bytearray(b'') |
| 37 | TaxsPayable | b'decimal(19,4)' | YES | bytearray(b'') |
| 29 | TotalAssets | b'decimal(19,4)' | YES | bytearray(b'') |
| 42 | TotalLiability | b'decimal(19,4)' | YES | bytearray(b'') |
| 44 | TotalShareholderEquity | b'decimal(19,4)' | YES | bytearray(b'') |



### mid_balancesheetall_indicator () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 10 | APDays | b'decimal(53,8)' | YES | bytearray(b'') |
| 8 | ARDays | b'decimal(55,8)' | YES | bytearray(b'') |
| 11 | CashDays | b'decimal(57,8)' | YES | bytearray(b'') |
| 2 | CompanyCode | b'int(11)' | NO | bytearray(b'') |
| 15 | Debt2Equity | b'decimal(52,8)' | YES | bytearray(b'') |
| 3 | EndDate | b'datetime' | NO | bytearray(b'') |
| 12 | FATurnover | b'decimal(51,8)' | YES | bytearray(b'') |
| 1 | InfoPublDate | b'datetime' | NO | bytearray(b'') |
| 9 | InvDays | b'decimal(53,8)' | YES | bytearray(b'') |
| 6 | LoanBondsLongterm | b'decimal(42,4)' | YES | bytearray(b'') |
| 7 | Purchase | b'decimal(44,4)' | YES | bytearray(b'') |
| 4 | Receivable | b'decimal(43,4)' | YES | bytearray(b'') |
| 14 | ROA | b'decimal(65,16)' | YES | bytearray(b'') |
| 17 | ROE | b'decimal(53,8)' | YES | bytearray(b'') |
| 5 | ShortTermDebt | b'decimal(42,4)' | YES | bytearray(b'') |
| 16 | TA2TE | b'decimal(49,8)' | YES | bytearray(b'') |
| 13 | TATurnover | b'decimal(51,8)' | YES | bytearray(b'') |



### mid_cashflowstatementall_basedata () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 8 | AccountingStandards | b'int(11)' | NO | bytearray(b'\xe4\xbc\x9a\xe8\xae\xa1\xe5\x87\x86\xe5\x88\x99') |
| 17 | BorrowingRepayment | b'decimal(19,4)' | YES | bytearray(b'') |
| 3 | BulletinType | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x91\x8a\xe7\xb1\xbb\xe5\x88\xab') |
| 14 | CashFromBondsIssue | b'decimal(19,4)' | YES | bytearray(b'') |
| 13 | CashFromBorrowing | b'decimal(19,4)' | YES | bytearray(b'') |
| 18 | CashFromInvest | b'decimal(19,4)' | YES | bytearray(b'') |
| 19 | CashFromMinoSInvestSub | b'decimal(19,4)' | YES | bytearray(b'') |
| 4 | CompanyCode | b'int(11)' | NO | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 15 | DividendInterestPayment | b'decimal(19,4)' | YES | bytearray(b'') |
| 5 | EndDate | b'datetime' | NO | bytearray(b'\xe6\x97\xa5\xe6\x9c\x9f') |
| 10 | FixIntanOtherAssetAcquiCash | b'decimal(19,4)' | YES | bytearray(b'') |
| 11 | FixIntanOtherAssetDispoCash | b'decimal(19,4)' | YES | bytearray(b'') |
| 12 | GoodsSaleServiceRenderCash | b'decimal(19,4)' | YES | bytearray(b'') |
| 1 | ID | b'bigint(20)' | NO | bytearray(b'ID') |
| 6 | IfAdjusted | b'int(11)' | NO | bytearray(b'\xe6\x98\xaf\xe5\x90\xa6\xe8\xb0\x83\xe6\x95\xb4') |
| 7 | IfMerged | b'int(11)' | NO | bytearray(b'\xe5\x90\x88\xe5\xb9\xb6\xe6\xa0\x87\xe5\xbf\x97') |
| 2 | InfoPublDate | b'datetime' | NO | bytearray(b'\xe4\xbf\xa1\xe6\x81\xaf\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f') |
| 9 | NetOperateCashFlow | b'decimal(19,4)' | YES | bytearray(b'') |
| 16 | ProceedsFromSubToMinoS | b'decimal(19,4)' | YES | bytearray(b'') |



### mid_cashflowstatementall_data () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 8 | AccountingStandards | b'bigint(12)' | YES | bytearray(b'') |
| 17 | BorrowingRepayment | b'decimal(20,4)' | YES | bytearray(b'') |
| 3 | BulletinType | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x91\x8a\xe7\xb1\xbb\xe5\x88\xab') |
| 14 | CashFromBondsIssue | b'decimal(20,4)' | YES | bytearray(b'') |
| 13 | CashFromBorrowing | b'decimal(20,4)' | YES | bytearray(b'') |
| 18 | CashFromInvest | b'decimal(20,4)' | YES | bytearray(b'') |
| 19 | CashFromMinoSInvestSub | b'decimal(20,4)' | YES | bytearray(b'') |
| 4 | CompanyCode | b'int(11)' | NO | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 15 | DividendInterestPayment | b'decimal(20,4)' | YES | bytearray(b'') |
| 5 | EndDate | b'datetime' | NO | bytearray(b'\xe6\x97\xa5\xe6\x9c\x9f') |
| 10 | FixIntanOtherAssetAcquiCash | b'decimal(20,4)' | YES | bytearray(b'') |
| 11 | FixIntanOtherAssetDispoCash | b'decimal(20,4)' | YES | bytearray(b'') |
| 12 | GoodsSaleServiceRenderCash | b'decimal(20,4)' | YES | bytearray(b'') |
| 1 | ID | b'bigint(20)' | NO | bytearray(b'ID') |
| 6 | IfAdjusted | b'int(11)' | NO | bytearray(b'\xe6\x98\xaf\xe5\x90\xa6\xe8\xb0\x83\xe6\x95\xb4') |
| 7 | IfMerged | b'int(11)' | NO | bytearray(b'\xe5\x90\x88\xe5\xb9\xb6\xe6\xa0\x87\xe5\xbf\x97') |
| 2 | InfoPublDate | b'datetime' | NO | bytearray(b'\xe4\xbf\xa1\xe6\x81\xaf\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f') |
| 9 | NetOperateCashFlow | b'decimal(20,4)' | YES | bytearray(b'') |
| 16 | ProceedsFromSubToMinoS | b'decimal(20,4)' | YES | bytearray(b'') |



### mid_cashflowstatementall_indicator () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | CapEx | b'decimal(43,4)' | YES | bytearray(b'') |
| 6 | CashSale | b'decimal(50,8)' | YES | bytearray(b'') |
| 7 | CFO2NI | b'decimal(53,8)' | YES | bytearray(b'') |
| 8 | CFO2OP | b'decimal(53,8)' | YES | bytearray(b'') |
| 2 | CompanyCode | b'int(11)' | NO | bytearray(b'') |
| 9 | DebtFinance | b'decimal(46,4)' | YES | bytearray(b'') |
| 3 | EndDate | b'datetime' | NO | bytearray(b'') |
| 10 | EquityFinance | b'decimal(44,4)' | YES | bytearray(b'') |
| 5 | FCF | b'decimal(44,4)' | YES | bytearray(b'') |
| 1 | InfoPublDate | b'datetime' | NO | bytearray(b'') |



### mid_fin_cfo2ni () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 8 | CFO2NI | b'decimal(45,8)' | YES | bytearray(b'') |
| 5 | ChiNameAbbr | b'varchar(100)' | YES | bytearray(b'\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d\xe7\xa7\xb0\xe7\xbc\xa9\xe5\x86\x99') |
| 1 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | EndDate | b'datetime' | YES | bytearray(b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f') |
| 6 | ListedDate | b'datetime' | YES | bytearray(b'\xe4\xb8\x8a\xe5\xb8\x82\xe6\x97\xa5\xe6\x9c\x9f') |
| 2 | ROE | b'decimal(19,4)' | YES | bytearray(b'ROE\xef\xbc\x88\xe5\xbd\x92\xe6\xaf\x8d\xe6\x9d\x83\xe7\x9b\x8a\xef\xbc\x89') |
| 7 | SecondIndustryName | b'varchar(100)' | YES | bytearray(b'\xe5\xaf\xb9\xe5\xba\x94\xe4\xba\x8c\xe7\xba\xa7\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0') |
| 4 | SecuCode | b'varchar(10)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe4\xbb\xa3\xe7\xa0\x81') |



### mid_fin_changepctry () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | ChangePCTRY | b'decimal(18,4)' | YES | bytearray(b'\xe5\x8d\x81\xe4\xba\x8c\xe4\xb8\xaa\xe6\x9c\x88\xe6\xb6\xa8\xe8\xb7\x8c\xe5\xb9\x85(%)1') |
| 2 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 1 | InnerCode | b'int(11)' | NO | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe5\x86\x85\xe9\x83\xa8\xe7\xbc\x96\xe7\xa0\x81') |
| 4 | SecondIndustryName | b'varchar(100)' | YES | bytearray(b'\xe5\xaf\xb9\xe5\xba\x94\xe4\xba\x8c\xe7\xba\xa7\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0') |



### mid_fin_changepctryrank () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | ChangePCTRY | b'decimal(18,4)' | YES | bytearray(b'\xe5\x8d\x81\xe4\xba\x8c\xe4\xb8\xaa\xe6\x9c\x88\xe6\xb6\xa8\xe8\xb7\x8c\xe5\xb9\x85(%)1') |
| 4 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | FirstIndustryName | b'varchar(100)' | YES | bytearray(b'') |
| 3 | InnerCode | b'int(11)' | NO | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe5\x86\x85\xe9\x83\xa8\xe7\xbc\x96\xe7\xa0\x81') |
| 1 | RankNumber | b'double' | YES | bytearray(b'') |



### mid_fin_debt2equity () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | Debt2Equity | b'decimal(65,12)' | YES | bytearray(b'') |
| 2 | EndDate | b'datetime' | YES | bytearray(b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f') |



### mid_fin_dimtime () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | companycode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | enddate | b'date' | NO | bytearray(b'\xe6\x97\xa5\xe6\x9c\x9f') |



### mid_fin_industry () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | companynum | b'bigint(21)' | NO | bytearray(b'') |
| 2 | EndDate | b'datetime' | YES | bytearray(b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f') |
| 6 | NetProfit | b'decimal(41,4)' | YES | bytearray(b'') |
| 5 | OperatingProfit | b'decimal(41,4)' | YES | bytearray(b'') |
| 4 | OperatingRevenue | b'decimal(41,4)' | YES | bytearray(b'') |
| 1 | SecondIndustryName | b'varchar(100)' | YES | bytearray(b'\xe5\xaf\xb9\xe5\xba\x94\xe4\xba\x8c\xe7\xba\xa7\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0') |



### mid_fin_industry_companycode () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | ChiNameAbbr | b'varchar(100)' | YES | bytearray(b'\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d\xe7\xa7\xb0\xe7\xbc\xa9\xe5\x86\x99') |
| 1 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | EndDate | b'datetime' | YES | bytearray(b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f') |
| 5 | ListedDate | b'datetime' | YES | bytearray(b'\xe4\xb8\x8a\xe5\xb8\x82\xe6\x97\xa5\xe6\x9c\x9f') |
| 9 | NetProfit | b'decimal(19,4)' | YES | bytearray(b'\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6') |
| 8 | OperatingProfit | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe5\x88\xa9\xe6\xb6\xa6') |
| 7 | OperatingRevenue | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5') |
| 6 | SecondIndustryName | b'varchar(100)' | YES | bytearray(b'\xe5\xaf\xb9\xe5\xba\x94\xe4\xba\x8c\xe7\xba\xa7\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0') |
| 3 | SecuCode | b'varchar(10)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe4\xbb\xa3\xe7\xa0\x81') |



### mid_fin_industry_companycode2 () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | ChiNameAbbr | b'varchar(100)' | YES | bytearray(b'\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d\xe7\xa7\xb0\xe7\xbc\xa9\xe5\x86\x99') |
| 1 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | EndDate | b'datetime' | YES | bytearray(b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f') |
| 5 | ListedDate | b'datetime' | YES | bytearray(b'\xe4\xb8\x8a\xe5\xb8\x82\xe6\x97\xa5\xe6\x9c\x9f') |
| 10 | Mark | b'int(1)' | NO | bytearray(b'') |
| 9 | NetProfit | b'decimal(19,4)' | YES | bytearray(b'\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6') |
| 8 | OperatingProfit | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe5\x88\xa9\xe6\xb6\xa6') |
| 7 | OperatingRevenue | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5') |
| 6 | SecondIndustryName | b'varchar(100)' | YES | bytearray(b'\xe5\xaf\xb9\xe5\xba\x94\xe4\xba\x8c\xe7\xba\xa7\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0') |
| 3 | SecuCode | b'varchar(10)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe4\xbb\xa3\xe7\xa0\x81') |



### mid_fin_industrylisteddate () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | ChiNameAbbr | b'varchar(100)' | YES | bytearray(b'\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d\xe7\xa7\xb0\xe7\xbc\xa9\xe5\x86\x99') |
| 1 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | EndDate | b'datetime' | YES | bytearray(b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f') |
| 5 | ListedDate | b'datetime' | YES | bytearray(b'\xe4\xb8\x8a\xe5\xb8\x82\xe6\x97\xa5\xe6\x9c\x9f') |
| 9 | NetProfit | b'decimal(19,4)' | YES | bytearray(b'\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6') |
| 8 | OperatingProfit | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe5\x88\xa9\xe6\xb6\xa6') |
| 7 | OperatingRevenue | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5') |
| 6 | SecondIndustryName | b'varchar(100)' | YES | bytearray(b'\xe5\xaf\xb9\xe5\xba\x94\xe4\xba\x8c\xe7\xba\xa7\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0') |
| 3 | SecuCode | b'varchar(10)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe4\xbb\xa3\xe7\xa0\x81') |



### mid_fin_industrynew () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | companynum | b'bigint(21)' | NO | bytearray(b'') |
| 2 | EndDate | b'datetime' | YES | bytearray(b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f') |
| 6 | NetProfit | b'decimal(41,4)' | YES | bytearray(b'') |
| 5 | OperatingProfit | b'decimal(41,4)' | YES | bytearray(b'') |
| 4 | OperatingRevenue | b'decimal(41,4)' | YES | bytearray(b'') |
| 1 | SecondIndustryName | b'varchar(100)' | YES | bytearray(b'\xe5\xaf\xb9\xe5\xba\x94\xe4\xba\x8c\xe7\xba\xa7\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0') |



### mid_fin_industrynewrate () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | companynum | b'bigint(23)' | YES | bytearray(b'') |
| 2 | EndDate | b'datetime' | YES | bytearray(b'') |
| 6 | NetProfit | b'decimal(52,8)' | YES | bytearray(b'') |
| 5 | OperatingProfit | b'decimal(52,8)' | YES | bytearray(b'') |
| 4 | OperatingRevenue | b'decimal(52,8)' | YES | bytearray(b'') |
| 1 | SecondIndustryName | b'varchar(100)' | YES | bytearray(b'') |



### mid_fin_industryrate () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | companynum | b'bigint(21)' | NO | bytearray(b'') |
| 2 | EndDate | b'datetime' | YES | bytearray(b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f') |
| 6 | NetProfit | b'decimal(50,8)' | YES | bytearray(b'') |
| 5 | OperatingProfit | b'decimal(50,8)' | YES | bytearray(b'') |
| 4 | OperatingRevenue | b'decimal(50,8)' | YES | bytearray(b'') |
| 1 | SecondIndustryName | b'varchar(100)' | YES | bytearray(b'\xe5\xaf\xb9\xe5\xba\x94\xe4\xba\x8c\xe7\xba\xa7\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0') |



### mid_fin_lc_qfinancialindexnewyear_data () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | AccountingStandards | b'int(11)' | YES | bytearray(b'\xe4\xbc\x9a\xe8\xae\xa1\xe5\x87\x86\xe5\x88\x99') |
| 12 | AdministrationExpense | b'decimal(41,4)' | YES | bytearray(b'') |
| 3 | BulletinType | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x91\x8a\xe7\xb1\xbb\xe5\x88\xab') |
| 23 | CashEquivalents | b'decimal(41,4)' | YES | bytearray(b'') |
| 4 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 22 | EffectiveTaxRate | b'decimal(41,4)' | YES | bytearray(b'') |
| 5 | EndDate | b'date' | YES | bytearray(b'') |
| 20 | FinancialExpense | b'decimal(41,4)' | YES | bytearray(b'') |
| 31 | FixedAssets | b'decimal(41,4)' | YES | bytearray(b'') |
| 15 | GoodsSaleServiceRenderCash | b'decimal(41,4)' | YES | bytearray(b'') |
| 1 | ID | b'bigint(20)' | YES | bytearray(b'ID') |
| 2 | InfoPublDate | b'datetime' | YES | bytearray(b'\xe4\xbf\xa1\xe6\x81\xaf\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f') |
| 28 | Inventories | b'decimal(41,4)' | YES | bytearray(b'') |
| 21 | InvestIncome | b'decimal(41,4)' | YES | bytearray(b'') |
| 25 | InvestmentProperty | b'decimal(41,4)' | YES | bytearray(b'') |
| 24 | LongtermEquityInvest | b'decimal(41,4)' | YES | bytearray(b'') |
| 6 | Mark | b'int(11)' | YES | bytearray(b'\xe5\x90\x88\xe5\xb9\xb6\xe8\xb0\x83\xe6\x95\xb4\xe6\xa0\x87\xe5\xbf\x97') |
| 16 | NetOperateCashFlow | b'decimal(41,4)' | YES | bytearray(b'') |
| 14 | NetProfit | b'decimal(41,4)' | YES | bytearray(b'') |
| 29 | NotAccountsPayable | b'decimal(41,4)' | YES | bytearray(b'') |
| 10 | NPParentCompanyOwners | b'decimal(41,4)' | YES | bytearray(b'') |
| 13 | OperatingCost | b'decimal(41,4)' | YES | bytearray(b'') |
| 11 | OperatingExpense | b'decimal(41,4)' | YES | bytearray(b'') |
| 9 | OperatingProfit | b'decimal(41,4)' | YES | bytearray(b'') |
| 8 | OperatingRevenue | b'decimal(41,4)' | YES | bytearray(b'') |
| 30 | Purchase | b'decimal(41,4)' | YES | bytearray(b'') |
| 27 | Receivable | b'decimal(41,4)' | YES | bytearray(b'') |
| 26 | SEWithoutMI | b'decimal(41,4)' | YES | bytearray(b'') |
| 17 | TotalAssets | b'decimal(41,4)' | YES | bytearray(b'') |
| 19 | TotalProfit | b'decimal(41,4)' | YES | bytearray(b'') |
| 18 | TotalShareholderEquity | b'decimal(41,4)' | YES | bytearray(b'') |



### mid_fin_lc_qfinancialindexnewyear_indicator () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 9 | AdministrationExpenseRate | b'decimal(65,8)' | YES | bytearray(b'') |
| 20 | APDays | b'decimal(65,8)' | YES | bytearray(b'') |
| 18 | ARDays | b'decimal(65,8)' | YES | bytearray(b'') |
| 13 | CashSale | b'decimal(65,8)' | YES | bytearray(b'') |
| 14 | CFO2NI | b'decimal(65,8)' | YES | bytearray(b'') |
| 2 | CompanyCode | b'int(11)' | YES | bytearray(b'') |
| 3 | EndDate | b'date' | YES | bytearray(b'') |
| 21 | FATurnover | b'decimal(65,8)' | YES | bytearray(b'') |
| 10 | GrossIncomeRatio | b'decimal(65,8)' | YES | bytearray(b'') |
| 1 | InfoPublDate | b'datetime' | YES | bytearray(b'') |
| 19 | InvDays | b'decimal(65,8)' | YES | bytearray(b'') |
| 4 | Mark | b'int(11)' | YES | bytearray(b'') |
| 12 | NetProfitRatio | b'decimal(65,8)' | YES | bytearray(b'') |
| 7 | NetProfitYOY | b'decimal(65,8)' | YES | bytearray(b'') |
| 8 | OperatingExpenseRate | b'decimal(65,8)' | YES | bytearray(b'') |
| 11 | OperatingProfitMargin | b'decimal(65,8)' | YES | bytearray(b'') |
| 6 | OperatingProfitYOY | b'decimal(65,8)' | YES | bytearray(b'') |
| 5 | OperatingRevenueYOY | b'decimal(65,8)' | YES | bytearray(b'') |
| 16 | ROA | b'decimal(65,12)' | YES | bytearray(b'') |
| 17 | ROE | b'decimal(65,8)' | YES | bytearray(b'') |
| 15 | TA2TE | b'decimal(65,8)' | YES | bytearray(b'') |
| 22 | TATurnover | b'decimal(65,8)' | YES | bytearray(b'') |



### mid_fin_operatingrevenue () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | ChiNameAbbr | b'varchar(100)' | YES | bytearray(b'\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d\xe7\xa7\xb0\xe7\xbc\xa9\xe5\x86\x99') |
| 1 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 5 | ListedDate | b'datetime' | YES | bytearray(b'\xe4\xb8\x8a\xe5\xb8\x82\xe6\x97\xa5\xe6\x9c\x9f') |
| 2 | OperatingRevenue | b'decimal(65,12)' | YES | bytearray(b'') |
| 6 | SecondIndustryName | b'varchar(100)' | YES | bytearray(b'\xe5\xaf\xb9\xe5\xba\x94\xe4\xba\x8c\xe7\xba\xa7\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0') |
| 3 | SecuCode | b'varchar(10)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe4\xbb\xa3\xe7\xa0\x81') |



### mid_fin_oryde () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | CFO2NI | b'decimal(45,8)' | YES | bytearray(b'') |
| 4 | ChiNameAbbr | b'varchar(100)' | YES | bytearray(b'\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d\xe7\xa7\xb0\xe7\xbc\xa9\xe5\x86\x99') |
| 1 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 9 | Debt2Equity | b'decimal(65,12)' | YES | bytearray(b'') |
| 5 | ListedDate | b'datetime' | YES | bytearray(b'\xe4\xb8\x8a\xe5\xb8\x82\xe6\x97\xa5\xe6\x9c\x9f') |
| 8 | OperatingRevenue | b'decimal(65,12)' | YES | bytearray(b'') |
| 2 | ROE | b'decimal(19,4)' | YES | bytearray(b'ROE\xef\xbc\x88\xe5\xbd\x92\xe6\xaf\x8d\xe6\x9d\x83\xe7\x9b\x8a\xef\xbc\x89') |
| 6 | SecondIndustryName | b'varchar(100)' | YES | bytearray(b'\xe5\xaf\xb9\xe5\xba\x94\xe4\xba\x8c\xe7\xba\xa7\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0') |
| 3 | SecuCode | b'varchar(10)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe4\xbb\xa3\xe7\xa0\x81') |



### mid_fin_rdinputrate () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | CapitalizedRDInputRAVG3Y | b'decimal(12,6)' | YES | bytearray(b'') |
| 1 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | EndDate | b'datetime' | NO | bytearray(b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f') |
| 4 | RDInputRatioAVG3Y | b'decimal(12,6)' | YES | bytearray(b'') |
| 3 | TotalRDInputAVG3Y | b'decimal(25,8)' | YES | bytearray(b'') |



### mid_fin_roe () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | ChiNameAbbr | b'varchar(100)' | YES | bytearray(b'\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d\xe7\xa7\xb0\xe7\xbc\xa9\xe5\x86\x99') |
| 1 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | EndDate | b'datetime' | YES | bytearray(b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f') |
| 6 | ListedDate | b'datetime' | YES | bytearray(b'\xe4\xb8\x8a\xe5\xb8\x82\xe6\x97\xa5\xe6\x9c\x9f') |
| 2 | ROE | b'decimal(19,4)' | YES | bytearray(b'ROE\xef\xbc\x88\xe5\xbd\x92\xe6\xaf\x8d\xe6\x9d\x83\xe7\x9b\x8a\xef\xbc\x89') |
| 7 | SecondIndustryName | b'varchar(100)' | YES | bytearray(b'\xe5\xaf\xb9\xe5\xba\x94\xe4\xba\x8c\xe7\xba\xa7\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0') |
| 4 | SecuCode | b'varchar(10)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe4\xbb\xa3\xe7\xa0\x81') |



### mid_fin_roeless () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 11 | CFO2NI | b'decimal(19,4)' | YES | bytearray(b'CFO/NI\xef\xbc\x88\xe7\xbb\x8f\xe8\x90\xa5\xe6\xb4\xbb\xe5\x8a\xa8\xe7\x8e\xb0\xe9\x87\x91\xe6\xb5\x81\xef\xbc\x89\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6') |
| 7 | ChiNameAbbr | b'varchar(100)' | YES | bytearray(b'\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d\xe7\xa7\xb0\xe7\xbc\xa9\xe5\x86\x99') |
| 5 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 4 | FirstIndustryName | b'varchar(100)' | YES | bytearray(b'') |
| 8 | ListedDate | b'datetime' | YES | bytearray(b'\xe4\xb8\x8a\xe5\xb8\x82\xe6\x97\xa5\xe6\x9c\x9f') |
| 1 | RankNumber | b'double' | YES | bytearray(b'') |
| 3 | RankRatio | b'double(22,4)' | YES | bytearray(b'') |
| 10 | ROE | b'decimal(19,4)' | YES | bytearray(b'ROE\xef\xbc\x88\xe5\xbd\x92\xe6\xaf\x8d\xe6\x9d\x83\xe7\x9b\x8a\xef\xbc\x89') |
| 9 | Score1 | b'decimal(14,1)' | YES | bytearray(b'') |
| 6 | SecuCode | b'varchar(10)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | sumNumber | b'bigint(21)' | YES | bytearray(b'') |



### mid_fin_singlecompany () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | ChiNameAbbr | b'varchar(100)' | YES | bytearray(b'\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d\xe7\xa7\xb0\xe7\xbc\xa9\xe5\x86\x99') |
| 1 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | EndDate | b'datetime' | YES | bytearray(b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f') |
| 5 | ListedDate | b'datetime' | YES | bytearray(b'\xe4\xb8\x8a\xe5\xb8\x82\xe6\x97\xa5\xe6\x9c\x9f') |
| 10 | Mark | b'int(1)' | NO | bytearray(b'') |
| 9 | NetProfit | b'decimal(19,4)' | YES | bytearray(b'\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6') |
| 8 | OperatingProfit | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe5\x88\xa9\xe6\xb6\xa6') |
| 7 | OperatingRevenue | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5') |
| 11 | RateMARK | b'int(1)' | NO | bytearray(b'') |
| 6 | SecondIndustryName | b'varchar(100)' | YES | bytearray(b'\xe5\xaf\xb9\xe5\xba\x94\xe4\xba\x8c\xe7\xba\xa7\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0') |
| 3 | SecuCode | b'varchar(10)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe4\xbb\xa3\xe7\xa0\x81') |



### mid_fin_singlecompanyrate () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | companynum | b'bigint(21)' | NO | bytearray(b'') |
| 1 | EndDate | b'datetime' | YES | bytearray(b'') |
| 6 | NetProfit | b'decimal(41,4)' | YES | bytearray(b'') |
| 5 | OperatingProfit | b'decimal(41,4)' | YES | bytearray(b'') |
| 4 | OperatingRevenue | b'decimal(41,4)' | YES | bytearray(b'') |
| 2 | SecondIndustryName | b'varchar(100)' | YES | bytearray(b'') |



### mid_fin_weicfo2ni () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | CFO2NI | b'decimal(45,8)' | YES | bytearray(b'') |
| 1 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | FirstIndustryName | b'varchar(100)' | YES | bytearray(b'\xe5\xaf\xb9\xe5\xba\x94\xe4\xb8\x80\xe7\xba\xa7\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0') |



### mid_fin_weicfo2niscore () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | CFO2NI | b'decimal(45,8)' | YES | bytearray(b'') |
| 4 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | FirstIndustryName | b'varchar(100)' | YES | bytearray(b'') |
| 1 | RankNumber | b'double' | YES | bytearray(b'') |
| 6 | Score | b'decimal(10,0)' | YES | bytearray(b'') |
| 2 | sumNumber | b'bigint(21)' | YES | bytearray(b'') |



### mid_fin_weioptprofityoy () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | FirstIndustryName | b'varchar(100)' | YES | bytearray(b'\xe5\xaf\xb9\xe5\xba\x94\xe4\xb8\x80\xe7\xba\xa7\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0') |
| 2 | OperatingProfitYOY | b'decimal(45,8)' | YES | bytearray(b'') |



### mid_fin_weioptprofityoyscore () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | FirstIndustryName | b'varchar(100)' | YES | bytearray(b'') |
| 5 | OperatingProfitYOY | b'decimal(45,8)' | YES | bytearray(b'') |
| 1 | RankNumber | b'double' | YES | bytearray(b'') |
| 6 | Score | b'decimal(10,0)' | YES | bytearray(b'') |
| 2 | sumNumber | b'bigint(21)' | YES | bytearray(b'') |



### mid_fin_weioptrevenue () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | FirstIndustryName | b'varchar(100)' | YES | bytearray(b'\xe5\xaf\xb9\xe5\xba\x94\xe4\xb8\x80\xe7\xba\xa7\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0') |
| 2 | OperatingRevenueYOY | b'decimal(45,8)' | YES | bytearray(b'') |



### mid_fin_weioptrevenuescore () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | FirstIndustryName | b'varchar(100)' | YES | bytearray(b'') |
| 5 | OperatingRevenueYOY | b'decimal(45,8)' | YES | bytearray(b'') |
| 1 | RankNumber | b'double' | YES | bytearray(b'') |
| 6 | Score | b'decimal(10,0)' | YES | bytearray(b'') |
| 2 | sumNumber | b'bigint(21)' | YES | bytearray(b'') |



### mid_fin_weiroe () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | FirstIndustryName | b'varchar(100)' | YES | bytearray(b'\xe5\xaf\xb9\xe5\xba\x94\xe4\xb8\x80\xe7\xba\xa7\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0') |
| 2 | ROE | b'decimal(45,8)' | YES | bytearray(b'') |



### mid_fin_weiroescore () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | FirstIndustryName | b'varchar(100)' | YES | bytearray(b'') |
| 1 | RankNumber | b'double' | YES | bytearray(b'') |
| 5 | ROE | b'decimal(45,8)' | YES | bytearray(b'') |
| 6 | Score | b'decimal(10,0)' | YES | bytearray(b'') |
| 2 | sumNumber | b'bigint(21)' | YES | bytearray(b'') |



### mid_fin_weiscore () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | ChiNameAbbr | b'varchar(100)' | YES | bytearray(b'\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d\xe7\xa7\xb0\xe7\xbc\xa9\xe5\x86\x99') |
| 2 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 1 | FirstIndustryName | b'varchar(100)' | YES | bytearray(b'') |
| 5 | ListedDate | b'datetime' | YES | bytearray(b'\xe4\xb8\x8a\xe5\xb8\x82\xe6\x97\xa5\xe6\x9c\x9f') |
| 6 | Score1 | b'decimal(14,1)' | YES | bytearray(b'') |
| 7 | Score2 | b'decimal(14,1)' | YES | bytearray(b'') |
| 8 | Score3 | b'decimal(14,1)' | YES | bytearray(b'') |
| 9 | Score4 | b'decimal(14,1)' | YES | bytearray(b'') |
| 3 | SecuCode | b'varchar(10)' | YES | bytearray(b'\xe8\xaf\x81\xe5\x88\xb8\xe4\xbb\xa3\xe7\xa0\x81') |



### mid_fut_memberrankbyoption_inc () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | contractcode | b'varchar(10)' | YES | bytearray(b'\xe5\x90\x88\xe7\xba\xa6\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | enddate | b'datetime' | NO | bytearray(b'\xe6\x97\xa5\xe6\x9c\x9f') |
| 4 | exchangecode | b'int(11)' | NO | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe6\x89\x80\xe4\xbb\xa3\xe7\xa0\x81') |
| 7 | indicatorCode | b'int(11)' | NO | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe5\x86\x85\xe9\x83\xa8\xe7\xbc\x96\xe7\xa0\x81') |
| 8 | indicatorName | b'varchar(50)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe5\x90\x8d\xe7\xa7\xb0') |
| 9 | indicatorVolume | b'decimal(18,4)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe9\x87\x8f(\xe6\x89\x8b)') |
| 11 | MemberAbbr | b'varchar(200)' | YES | bytearray(b'\xe4\xbc\x9a\xe5\x91\x98\xe7\xae\x80\xe7\xa7\xb0') |
| 10 | MemberCode | b'varchar(20)' | YES | bytearray(b'\xe4\xbc\x9a\xe5\x91\x98\xe5\x8f\xb7') |
| 5 | OptionCode | b'int(11)' | YES | bytearray(b'\xe5\x93\x81\xe7\xa7\x8d\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | STR | b'varchar(41)' | YES | bytearray(b'') |
| 1 | SumIndicatorVolume | b'decimal(40,4)' | YES | bytearray(b'') |
| 12 | TradingCode | b'varchar(100)' | YES | bytearray(b'') |



### mid_incomestatementall_basedate () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 8 | AccountingStandards | b'int(11)' | NO | bytearray(b'\xe4\xbc\x9a\xe8\xae\xa1\xe5\x87\x86\xe5\x88\x99') |
| 14 | AdministrationExpense | b'decimal(19,4)' | YES | bytearray(b'') |
| 15 | AssetImpairmentLoss | b'decimal(19,4)' | YES | bytearray(b'') |
| 3 | BulletinType | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x91\x8a\xe7\xb1\xbb\xe5\x88\xab') |
| 4 | CompanyCode | b'int(11)' | NO | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 5 | EndDate | b'datetime' | NO | bytearray(b'\xe6\x97\xa5\xe6\x9c\x9f') |
| 9 | EnterpriseType | b'int(11)' | NO | bytearray(b'\xe5\xb7\xa5\xe4\xb8\x9a\xe4\xbc\x81\xe4\xb8\x9a\xe7\xb1\xbb\xe5\x9e\x8b') |
| 16 | FinancialExpense | b'decimal(19,4)' | YES | bytearray(b'') |
| 23 | GrossIncomeRatio | b'decimal(22,8)' | YES | bytearray(b'') |
| 1 | ID | b'bigint(20)' | NO | bytearray(b'ID') |
| 6 | IfAdjusted | b'int(11)' | NO | bytearray(b'\xe6\x98\xaf\xe5\x90\xa6\xe8\xb0\x83\xe6\x95\xb4') |
| 7 | IfMerged | b'int(11)' | NO | bytearray(b'\xe5\x90\x88\xe5\xb9\xb6\xe6\xa0\x87\xe5\xbf\x97') |
| 19 | IncomeTaxCost | b'decimal(19,4)' | YES | bytearray(b'') |
| 2 | InfoPublDate | b'datetime' | NO | bytearray(b'\xe4\xbf\xa1\xe6\x81\xaf\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f') |
| 17 | InvestIncome | b'decimal(19,4)' | YES | bytearray(b'') |
| 20 | NetProfit | b'decimal(19,4)' | YES | bytearray(b'') |
| 25 | NetProfitRatio | b'decimal(22,8)' | YES | bytearray(b'') |
| 26 | NetProfitYOY | b'decimal(22,8)' | YES | bytearray(b'') |
| 21 | NPParentCompanyOwners | b'decimal(19,4)' | YES | bytearray(b'') |
| 11 | OperatingCost | b'decimal(19,4)' | YES | bytearray(b'') |
| 13 | OperatingExpense | b'decimal(19,4)' | YES | bytearray(b'') |
| 24 | OperatingExpenseRate | b'decimal(22,8)' | YES | bytearray(b'') |
| 10 | OperatingRevenue | b'decimal(19,4)' | YES | bytearray(b'') |
| 22 | OperatingRevenueYOY | b'decimal(22,8)' | YES | bytearray(b'') |
| 12 | OperatingTaxSurcharges | b'decimal(19,4)' | YES | bytearray(b'') |
| 27 | RAndD | b'decimal(19,4)' | YES | bytearray(b'') |
| 18 | TotalProfit | b'decimal(19,4)' | YES | bytearray(b'') |



### mid_incomestatementall_date () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 8 | AccountingStandards | b'int(11)' | NO | bytearray(b'\xe4\xbc\x9a\xe8\xae\xa1\xe5\x87\x86\xe5\x88\x99') |
| 14 | AdministrationExpense | b'decimal(20,4)' | YES | bytearray(b'') |
| 15 | AssetImpairmentLoss | b'decimal(20,4)' | YES | bytearray(b'') |
| 3 | BulletinType | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x91\x8a\xe7\xb1\xbb\xe5\x88\xab') |
| 4 | CompanyCode | b'int(11)' | NO | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 5 | EndDate | b'datetime' | NO | bytearray(b'\xe6\x97\xa5\xe6\x9c\x9f') |
| 9 | EnterpriseType | b'int(11)' | NO | bytearray(b'\xe5\xb7\xa5\xe4\xb8\x9a\xe4\xbc\x81\xe4\xb8\x9a\xe7\xb1\xbb\xe5\x9e\x8b') |
| 16 | FinancialExpense | b'decimal(20,4)' | YES | bytearray(b'') |
| 24 | GrossIncomeRatio | b'decimal(22,8)' | YES | bytearray(b'') |
| 1 | ID | b'bigint(20)' | NO | bytearray(b'ID') |
| 6 | IfAdjusted | b'int(11)' | NO | bytearray(b'\xe6\x98\xaf\xe5\x90\xa6\xe8\xb0\x83\xe6\x95\xb4') |
| 7 | IfMerged | b'int(11)' | NO | bytearray(b'\xe5\x90\x88\xe5\xb9\xb6\xe6\xa0\x87\xe5\xbf\x97') |
| 19 | IncomeTaxCost | b'decimal(20,4)' | YES | bytearray(b'') |
| 2 | InfoPublDate | b'datetime' | NO | bytearray(b'\xe4\xbf\xa1\xe6\x81\xaf\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f') |
| 17 | InvestIncome | b'decimal(20,4)' | YES | bytearray(b'') |
| 20 | NetProfit | b'decimal(20,4)' | YES | bytearray(b'') |
| 26 | NetProfitRatio | b'decimal(22,8)' | YES | bytearray(b'') |
| 27 | NetProfitYOY | b'decimal(22,8)' | YES | bytearray(b'') |
| 21 | NPParentCompanyOwners | b'decimal(20,4)' | YES | bytearray(b'') |
| 11 | OperatingCost | b'decimal(20,4)' | YES | bytearray(b'') |
| 13 | OperatingExpense | b'decimal(20,4)' | YES | bytearray(b'') |
| 25 | OperatingExpenseRate | b'decimal(22,8)' | YES | bytearray(b'') |
| 10 | OperatingRevenue | b'decimal(20,4)' | YES | bytearray(b'') |
| 23 | OperatingRevenueYOY | b'decimal(22,8)' | YES | bytearray(b'') |
| 12 | OperatingTaxSurcharges | b'decimal(20,4)' | YES | bytearray(b'') |
| 22 | RAndD | b'decimal(20,4)' | YES | bytearray(b'') |
| 18 | TotalProfit | b'decimal(20,4)' | YES | bytearray(b'') |



### mid_incomestatementall_indicator () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 10 | AdministrationExpenseRate | b'decimal(50,8)' | YES | bytearray(b'') |
| 9 | AdministrationExpenseYOY | b'decimal(51,8)' | YES | bytearray(b'') |
| 2 | CompanyCode | b'int(11)' | NO | bytearray(b'') |
| 15 | EffectiveTaxRate | b'decimal(50,8)' | YES | bytearray(b'') |
| 3 | EndDate | b'datetime' | NO | bytearray(b'') |
| 4 | IfAdjusted | b'int(11)' | NO | bytearray(b'') |
| 5 | IfMerged | b'int(11)' | NO | bytearray(b'') |
| 1 | InfoPublDate | b'datetime' | NO | bytearray(b'') |
| 8 | OperatingExpenseYOY | b'decimal(51,8)' | YES | bytearray(b'') |
| 6 | OperatingPayoutYOY | b'decimal(51,8)' | YES | bytearray(b'') |
| 11 | OperatingProfit | b'decimal(47,4)' | YES | bytearray(b'') |
| 13 | OperatingProfitMargin | b'decimal(55,8)' | YES | bytearray(b'') |
| 12 | OperatingProfitYOY | b'decimal(56,8)' | YES | bytearray(b'') |
| 7 | OperatingTaxSurchargesYOY | b'decimal(50,8)' | YES | bytearray(b'') |
| 17 | RAndDRate | b'decimal(50,8)' | YES | bytearray(b'') |
| 16 | RAndDYOY | b'decimal(51,8)' | YES | bytearray(b'') |
| 14 | TotalProfitYOY | b'decimal(51,8)' | YES | bytearray(b'') |



### physicians-per-1000-people (1) () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | Code | b'varchar(255)' | YES | bytearray(b'') |
| 1 | Entity | b'varchar(255)' | YES | bytearray(b'') |
| 4 | Physicians (per 1,000 people) (per 1,000 people) | b'decimal(20,4)' | YES | bytearray(b'') |
| 3 | Year | b'varchar(255)' | YES | bytearray(b'') |



### s01_cn_fut_positionranking () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | BBTicker | b'varchar(15)' | YES | bytearray(b'Bloomberg\xe4\xbb\xa3\xe7\xa0\x81') |
| 1 | FutCode | b'varchar(15)' | NO | bytearray(b'\xe5\x90\x88\xe7\xba\xa6\xe4\xbb\xa3\xe7\xa0\x81') |
| 9 | LBroker | b'varchar(20)' | YES | bytearray(b'\xe4\xb9\xb0\xe5\x8d\x95\xe7\x9b\xb8\xe5\x85\xb3\xe6\x9c\x9f\xe8\xb4\xa7\xe5\x85\xac\xe5\x8f\xb8') |
| 10 | LDailyChange | b'int(11)' | YES | bytearray(b'\xe4\xb9\xb0\xe5\x8d\x95\xe9\x87\x8f\xe5\x8f\x98\xe5\x8c\x96') |
| 8 | LongPosition | b'int(11)' | YES | bytearray(b'\xe6\x8c\x81\xe4\xb9\xb0\xe5\x8d\x95\xe9\x87\x8f') |
| 15 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 18 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 16 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 4 | Ranking | b'int(11)' | NO | bytearray(b'\xe6\x8e\x92\xe5\x90\x8d') |
| 12 | SBroker | b'varchar(20)' | YES | bytearray(b'\xe5\x8d\x96\xe5\x8d\x95\xe7\x9b\xb8\xe5\x85\xb3\xe6\x9c\x9f\xe8\xb4\xa7\xe5\x85\xac\xe5\x8f\xb8') |
| 13 | SDailyChange | b'int(11)' | YES | bytearray(b'\xe5\x8d\x96\xe5\x8d\x95\xe5\x8f\x98\xe5\x8c\x96') |
| 11 | ShortPosition | b'int(11)' | YES | bytearray(b'\xe6\x8c\x81\xe5\x8d\x96\xe5\x8d\x95\xe9\x87\x8f') |
| 17 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 14 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 3 | Tradingday | b'datetime' | NO | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe6\x97\xa5') |
| 19 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 5 | VBroker | b'varchar(20)' | YES | bytearray(b'\xe6\x88\x90\xe4\xba\xa4\xe9\x87\x8f\xe7\x9b\xb8\xe5\x85\xb3\xe6\x9c\x9f\xe8\xb4\xa7\xe5\x85\xac\xe5\x8f\xb8') |
| 7 | VDailyChange | b'int(11)' | YES | bytearray(b'\xe6\x88\x90\xe4\xba\xa4\xe9\x87\x8f\xe5\x8f\x98\xe5\x8c\x96') |
| 6 | Volume | b'int(11)' | YES | bytearray(b'\xe6\x88\x90\xe4\xba\xa4\xe9\x87\x8f') |



### s01_mfile_yanbao_file () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | File_Id | b'varchar(100)' | NO | bytearray(b'') |
| 3 | File_Name | b'varchar(200)' | NO | bytearray(b'') |
| 13 | File_Path | b'varchar(100)' | NO | bytearray(b'') |
| 7 | File_Type | b'varchar(10)' | NO | bytearray(b'') |
| 14 | From_Mail | b'varchar(50)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 9 | Level_Power | b'int(11)' | NO | bytearray(b'') |
| 11 | Make_Datetime | b'datetime(6)' | NO | bytearray(b'') |
| 6 | Recv_Grandson_Source | b'varchar(30)' | NO | bytearray(b'') |
| 5 | Recv_Son_Source | b'varchar(30)' | NO | bytearray(b'') |
| 4 | Recv_Source | b'varchar(30)' | NO | bytearray(b'') |
| 10 | Tag | b'varchar(10)' | NO | bytearray(b'') |
| 8 | Title | b'varchar(200)' | NO | bytearray(b'') |
| 12 | UpDatetime | b'datetime(6)' | NO | bytearray(b'') |



### s01_onorder () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | direction | b'varchar(20)' | NO | bytearray(b'') |
| 16 | exchangeid | b'varchar(10)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 14 | inserttime | b'varchar(20)' | NO | bytearray(b'') |
| 5 | instrumentid | b'varchar(20)' | NO | bytearray(b'') |
| 2 | investorid | b'varchar(20)' | NO | bytearray(b'') |
| 8 | limitprice | b'decimal(30,15)' | NO | bytearray(b'') |
| 15 | localdate | b'datetime(6)' | NO | bytearray(b'') |
| 7 | offsetflag | b'varchar(20)' | NO | bytearray(b'') |
| 10 | orderstatus | b'varchar(1)' | NO | bytearray(b'') |
| 4 | ordersysid | b'varchar(30)' | NO | bytearray(b'') |
| 3 | userid | b'varchar(20)' | NO | bytearray(b'') |
| 17 | userorderlocalid | b'varchar(20)' | NO | bytearray(b'') |
| 9 | volume | b'int(11)' | NO | bytearray(b'') |
| 13 | volumecancled | b'int(11)' | NO | bytearray(b'') |
| 12 | volumeremain | b'int(11)' | NO | bytearray(b'') |
| 11 | volumetraded | b'int(11)' | NO | bytearray(b'') |



### s01_proxyip () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | Available | b'int(11)' | YES | bytearray(b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\xaf\xe7\x94\xa8') |
| 1 | IP | b'varchar(15)' | NO | bytearray(b'IP\xe5\x9c\xb0\xe5\x9d\x80') |
| 4 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 2 | Port | b'varchar(15)' | YES | bytearray(b'\xe7\xab\xaf\xe5\x8f\xa3\xe5\x8f\xb7') |
| 3 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 6 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_tb_emp () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | contract_info | b'varchar(20000)' | NO | bytearray(b'') |
| 2 | contract_name | b'varchar(20)' | NO | bytearray(b'') |
| 4 | contract_using | b'tinyint(1)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |



### s01_tb_investorid () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 2 | investorid | b'varchar(20)' | NO | bytearray(b'') |



### s01_tbmics () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 2 | INDEX_OF_CONSUMER_SENTIMENT | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_trading () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | direction_stop | b'longtext' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 2 | investorid | b'varchar(20)' | NO | bytearray(b'') |
| 6 | pricetick | b'decimal(18,8)' | NO | bytearray(b'') |
| 3 | ticker | b'varchar(10)' | NO | bytearray(b'') |
| 5 | volumes | b'int(11)' | NO | bytearray(b'') |



### s01_untitled () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 8 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 7 | Equals_Final_sales_to_domestic_purchasers | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Equals_Gross_domestic_purchases | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Final_sales_of_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Final_sales_to_private_domestic_purchasers1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Less_Change_in_private_inventories | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Less_Exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 15 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 13 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 4 | Plus_Imports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 11 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 16 | Updatetime | b'datetime' | YES | bytearray(b'') |



### s01_us_building_expenditure_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 51 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 54 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 52 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 30 | Private_Amusement_and_recreation | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Private_Commercial | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Private_Communication | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Private_Educational | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Private_Health_care | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Private_Lodging | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Private_Manufacturing | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Private_Nonresidential | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Private_Office | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Private_Power | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Private_Religious | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Private_Residential | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Private_Transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Public_Amusement_and_recreation | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Public_Commercial | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | Public_Educational | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Public_Health_care | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Public_Highway_and_street | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Public_Nonresidential | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Public_Office | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Public_Power | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Public_Public_safety | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Public_Residential | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Public_Transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | PublicConservation_and_development | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | PublicSewage_and_waste_disposal | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | PublicWater_supply | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 50 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 12 | Total_Amusement_and_recreation | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Total_Commercial | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Total_Communication | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Total_Conservation_and_development | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Total_Construction | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Total_Educational | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Total_Health_care | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Total_Highway_and_street | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Total_Lodging | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Total_Manufacturing | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Total_Nonresidential | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Total_Office | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Total_Power | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Total_Private_Construction | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Total_Public_Construction | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Total_Public_safety | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Total_Religious | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Total_Residential | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Total_Sewage_and_waste_disposal | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Total_Transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Total_Water_supply | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_commercial_bank_assets_and_liabilities_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 38 | B_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | B_c_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | C_a_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | C_a_i_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | C_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | C_l_C_c_a_o_r_p_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | C_l_O_c_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | C_l_O_c_l_A_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | C_l_O_c_l_A_o_c_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | D_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 31 | F_f_s_a_s_p_u_a_t_r | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | L_A_f_l_a_l_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | L_a_l_i_b_c_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | L_t_c_b_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | L_t_d_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 39 | N_d_t_r_f_o_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | N_u_g_l_o_a_f_s_s_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | O_a_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | O_d_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | O_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | O_l_a_l_A_o_l_a_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | O_l_a_l_A_o_l_a_l_L_t_n_f_i_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | O_l_a_l_A_o_l_a_l_O_l_n_e_c_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | O_s_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | O_s_M_b_s_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | O_s_N_M_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 47 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 42 | R_a_l_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | R_e_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | R_e_l_C_r_e_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | R_e_l_C_r_e_l_C_a_l_d_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | R_e_l_C_r_e_l_S_b_f_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | R_e_l_C_r_e_l_S_b_m_p_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | R_e_l_C_r_e_l_S_b_n_n_p_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | R_e_l_R_r_e_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | R_e_l_R_r_e_l_C_e_r_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | R_e_l_R_r_e_l_R_h_e_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | S_i_b_c_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 45 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 34 | T_a_a_o_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | T_a_a_s_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | T_a_a_s_M_b_s_M_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | T_a_a_s_N_M_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | T_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | U_S_T_a_a_s_M_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'') |
| 50 | Updatetime | b'datetime' | YES | bytearray(b'') |



### s01_us_corporate_profits_by_industry_a () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 27 | Chemical_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Computer_and_electronic_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Corporate_profits_with_inventory_valuation_adjustment | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | CorporateProfits_InventVal_CapitalConAdj | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 3 | Domestic_industries_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Domestic_industries_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Electrical_equipment_appliances_and_components | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Fabricated_metal_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Federal_Reserve_banks | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Financial | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Financial1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Food_and_beverage_and_tobacco_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Information | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Less_Payments_to_the_rest_of_the_world | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Machinery | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Manufacturing | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 22 | Motor_vehicles_bodies_and_trailers_and_parts | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Nonfinancial_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Nonfinancial_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 23 | Other_durable_goods3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Other_financial2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Other_nondurable_goods4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Other_nonfinancial5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 26 | Petroleum_and_coal_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Receipts_from_the_rest_of_the_world | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Rest_of_the_world_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Rest_of_the_world_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Retail_trade | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 35 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 31 | Transportation_and_warehousing | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Updatetime | b'datetime' | YES | bytearray(b'') |
| 15 | Utilities | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Wholesale_trade | b'decimal(18,4)' | YES | bytearray(b'') |



### s01_us_corporate_profits_by_industry_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 27 | Chemical_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Computer_and_electronic_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Corporate_profits_with_inventory_valuation_adjustment | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | CorporateProfits_InventVal_CapitalConAdj | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 3 | Domestic_industries_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Domestic_industries_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Electrical_equipment_appliances_and_components | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Fabricated_metal_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Federal_Reserve_banks | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Financial | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Financial1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Food_and_beverage_and_tobacco_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Information | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Less_Payments_to_the_rest_of_the_world | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Machinery | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Manufacturing | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 22 | Motor_vehicles_bodies_and_trailers_and_parts | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Nonfinancial_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Nonfinancial_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 23 | Other_durable_goods3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Other_financial2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Other_nondurable_goods4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Other_nonfinancial5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 26 | Petroleum_and_coal_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Receipts_from_the_rest_of_the_world | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Rest_of_the_world_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Rest_of_the_world_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Retail_trade | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 35 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 31 | Transportation_and_warehousing | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Updatetime | b'datetime' | YES | bytearray(b'') |
| 15 | Utilities | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Wholesale_trade | b'decimal(18,4)' | YES | bytearray(b'') |



### s01_us_domestic_buyer_final_sales_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 8 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 7 | Equals_Final_sales_to_domestic_purchasers | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Equals_Gross_domestic_purchases | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Final_sales_of_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Final_sales_to_private_domestic_purchasers1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Less_Change_in_private_inventories | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Less_Exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 15 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 13 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 4 | Plus_Imports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 11 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 16 | Updatetime | b'datetime' | YES | bytearray(b'') |



### s01_us_employment_cost_index_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 2 | Employment_cost_index | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_esms_seasonallyadjusted_diffusion () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 11 | AWCDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | AWFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | CEFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 6 | DTCDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | DTFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | GACDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | GAFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | IVCDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | IVFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 10 | NECDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | NEFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | NOCDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | NOFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 26 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | PPCDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | PPFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | PRCDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | PRFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | SHCDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | SHFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 24 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 23 | TSFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | UOCDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | UOFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_export_price () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | All_exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Automotive_vehicles_parts_and_engines | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Capital_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Consumer_goods_excluding_automotives | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 3 | Foods_feeds_and_beverages | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Industrial_supplies_and_materials | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 12 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 10 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 11 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 8 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 13 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_foreign_trade_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 35 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Balance_on_current_account_NIPAs_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Balance_on_current_account_NIPAs_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | C_t_c_f_g_s_i_a_t_r_f_t_r_o_t_w | b'decimal(18,4)' | YES | bytearray(b'Current_taxes_contributions_for_government_social_insurance_and_transfer_receipts_from_the_rest_of_the_world2') |
| 18 | Current_payments_to_the_rest_of_the_world | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Current_receipts_from_the_rest_of_the_world | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Current_taxes_and_transfer_payments_to_the_rest_of_the_world2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 12 | Dividends_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Dividends_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Durable_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Durable_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | From_business | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | From_government | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | From_persons | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Imports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Income_payments | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Income_payments_on_assets | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Income_receipts | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Income_receipts_on_assets | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Interest_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Interest_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Less_Capital_account_transactions_net_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 36 | Net_lending_or_net_borrowing_NIPAs | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Nondurable_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Nondurable_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 41 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 29 | R_e_o_f_d_i_i_t_U_S | b'decimal(18,4)' | YES | bytearray(b'Reinvested_earnings_on_foreign_direct_investment_in_the_United_States') |
| 13 | Reinvested_earnings_on_U_S_direct_investment_abroad | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Services_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Services_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 39 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 16 | To_business | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | To_government | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | To_persons | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 25 | Wage_and_salary_payments | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Wage_and_salary_receipts | b'decimal(18,4)' | YES | bytearray(b'') |



### s01_us_foreign_trade_y () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 35 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Balance_on_current_account_NIPAs_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Balance_on_current_account_NIPAs_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | C_t_c_f_g_s_i_a_t_r_f_t_r_o_t_w | b'decimal(18,4)' | YES | bytearray(b'Current_taxes_contributions_for_government_social_insurance_and_transfer_receipts_from_the_rest_of_the_world2') |
| 18 | Current_payments_to_the_rest_of_the_world | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Current_receipts_from_the_rest_of_the_world | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Current_taxes_and_transfer_payments_to_the_rest_of_the_world2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 12 | Dividends_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Dividends_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Durable_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Durable_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | From_business | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | From_government | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | From_persons | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Imports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Income_payments | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Income_payments_on_assets | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Income_receipts | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Income_receipts_on_assets | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Interest_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Interest_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Less_Capital_account_transactions_net_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 36 | Net_lending_or_net_borrowing_NIPAs | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Nondurable_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Nondurable_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 41 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 29 | R_e_o_f_d_i_i_t_U_S | b'decimal(18,4)' | YES | bytearray(b'Reinvested_earnings_on_foreign_direct_investment_in_the_United_States') |
| 13 | Reinvested_earnings_on_U_S_direct_investment_abroad | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Services_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Services_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 39 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 16 | To_business | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | To_government | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | To_persons | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 25 | Wage_and_salary_payments | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Wage_and_salary_receipts | b'decimal(18,4)' | YES | bytearray(b'') |



### s01_us_frb_g17_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | Value | b'decimal(18,4)' | YES | bytearray(b'') |



### s01_us_frb_g17_y () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | Value | b'decimal(18,4)' | YES | bytearray(b'') |



### s01_us_frb_h8 () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | B1001NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | B1002NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | B1003NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | B1011NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | B1020NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | B1023NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | B1026NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | B1027NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | B1029NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | B1030NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | B1043NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | B1047NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | B1048NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | B1058NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | B1072NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | B1091NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | B1100NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | B1110NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | B1151NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | B1152NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | B1215NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | B1216NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | B1217NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | B1218NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | B1220NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | B1221NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | B1231NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | B1243NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | B1245NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | B1247NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | B1301NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | B1302NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | B1303NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | B1304NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | B1310NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | B3053NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | B3092NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | B3094NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | B3095NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | B3219NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | B3248NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | B3305NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | B8321NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 46 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 49 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 47 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 48 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 45 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 50 | Updatetime | b'datetime' | YES | bytearray(b'') |



### s01_us_gdp_a () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 15 | Change_in_private_inventories | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 5 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Federal | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Fixed_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Government_consumption_expenditures_and_gross_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Gross_private_domestic_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Intellectual_property_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 25 | National_defense | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Net_exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Nondefense | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Nonresidential | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 30 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 3 | Personal_consumption_expenditures | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Residential | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Services | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Services_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Services_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 28 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 27 | State_and_local | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Structures | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_gdp_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 15 | Change_in_private_inventories | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 5 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Federal | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Fixed_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Government_consumption_expenditures_and_gross_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Gross_private_domestic_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Intellectual_property_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 25 | National_defense | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Net_exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Nondefense | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Nonresidential | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 30 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 3 | Personal_consumption_expenditures | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Residential | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Services | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Services_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Services_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 28 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 27 | State_and_local | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Structures | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_import_and_export_by_product_category_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 50 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Automotive_vehicles_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Automotive_vehicles_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Capital_goods_except_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Capital_goods_except_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Charges_for_the_use_of_intellectual_property_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Charges_for_the_use_of_intellectual_property_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Civilian_aircraft_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Civilian_aircraft_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Computers_peripherals_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Computers_peripherals_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Consumer_goods_except_food_and_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Consumer_goods_except_food_and_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 6 | Durable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Durable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Durable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Durable_goods_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Exports_of_agricultural_goods4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 51 | Exports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Exports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 54 | Exports_of_nonagricultural_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 52 | Exports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Exports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Foods_feeds_and_beverages_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Foods_feeds_and_beverages_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Government_goods_and_services_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Government_goods_and_services_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | Imports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Imports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Imports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 56 | Imports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 57 | Imports_of_nonpetroleum_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Imports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Industrial_supplies_and_materials_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Industrial_supplies_and_materials_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 59 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Nondurable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Nondurable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Nondurable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | Nondurable_goods_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Nondurable_goods_excluding_petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Nondurable_goods_excluding_petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 62 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 18 | Other2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Other_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Other_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Other_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Other_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Other_5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Other_business_services3_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Other_business_services3_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 60 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | Petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 61 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 58 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 20 | Transport_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Transport_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Travel_for_all_purposes_including_education_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Travel_for_all_purposes_including_education_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 63 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_import_and_export_by_product_category_y () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 50 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Automotive_vehicles_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Automotive_vehicles_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Capital_goods_except_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Capital_goods_except_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Charges_for_the_use_of_intellectual_property_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Charges_for_the_use_of_intellectual_property_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Civilian_aircraft_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Civilian_aircraft_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Computers_peripherals_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Computers_peripherals_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Consumer_goods_except_food_and_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Consumer_goods_except_food_and_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 6 | Durable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Durable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Durable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Durable_goods_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Exports_of_agricultural_goods4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 51 | Exports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Exports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 54 | Exports_of_nonagricultural_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 52 | Exports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Exports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Foods_feeds_and_beverages_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Foods_feeds_and_beverages_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Government_goods_and_services_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Government_goods_and_services_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | Imports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Imports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Imports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 56 | Imports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 57 | Imports_of_nonpetroleum_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Imports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Industrial_supplies_and_materials_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Industrial_supplies_and_materials_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 59 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Nondurable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Nondurable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Nondurable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | Nondurable_goods_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Nondurable_goods_excluding_petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Nondurable_goods_excluding_petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 62 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 18 | Other2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Other_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Other_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Other_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Other_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Other_5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Other_business_services3_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Other_business_services3_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 60 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | Petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 61 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 58 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 20 | Transport_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Transport_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Travel_for_all_purposes_including_education_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Travel_for_all_purposes_including_education_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 63 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_import_and_export_price_index_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 50 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Automotive_vehicles_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Automotive_vehicles_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Capital_goods_except_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Capital_goods_except_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Charges_for_the_use_of_intellectual_property_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Charges_for_the_use_of_intellectual_property_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Civilian_aircraft_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Civilian_aircraft_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Computers_peripherals_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Computers_peripherals_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Consumer_goods_except_food_and_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Consumer_goods_except_food_and_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 6 | Durable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Durable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Durable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Durable_goods_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Exports_of_agricultural_goods4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 51 | Exports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Exports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 54 | Exports_of_nonagricultural_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 52 | Exports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Exports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Foods_feeds_and_beverages_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Foods_feeds_and_beverages_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Government_goods_and_services_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Government_goods_and_services_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | Imports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Imports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Imports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 56 | Imports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 57 | Imports_of_nonpetroleum_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Imports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Industrial_supplies_and_materials_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Industrial_supplies_and_materials_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 59 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Nondurable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Nondurable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Nondurable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | Nondurable_goods_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Nondurable_goods_excluding_petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Nondurable_goods_excluding_petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 62 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 18 | Other2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Other_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Other_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Other_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Other_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Other_5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Other_business_services3_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Other_business_services3_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 60 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | Petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 61 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 58 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 20 | Transport_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Transport_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Travel_for_all_purposes_including_education_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Travel_for_all_purposes_including_education_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 63 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_import_and_export_price_index_y () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 50 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Automotive_vehicles_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Automotive_vehicles_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Capital_goods_except_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Capital_goods_except_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Charges_for_the_use_of_intellectual_property_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Charges_for_the_use_of_intellectual_property_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Civilian_aircraft_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Civilian_aircraft_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Computers_peripherals_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Computers_peripherals_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Consumer_goods_except_food_and_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Consumer_goods_except_food_and_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 6 | Durable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Durable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Durable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Durable_goods_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Exports_of_agricultural_goods4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 51 | Exports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Exports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 54 | Exports_of_nonagricultural_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 52 | Exports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Exports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Foods_feeds_and_beverages_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Foods_feeds_and_beverages_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Government_goods_and_services_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Government_goods_and_services_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | Imports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Imports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Imports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 56 | Imports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 57 | Imports_of_nonpetroleum_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Imports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Industrial_supplies_and_materials_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Industrial_supplies_and_materials_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 59 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Nondurable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Nondurable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Nondurable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | Nondurable_goods_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Nondurable_goods_excluding_petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Nondurable_goods_excluding_petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 62 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 18 | Other2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Other_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Other_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Other_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Other_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Other_5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Other_business_services3_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Other_business_services3_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 60 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | Petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 61 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 58 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 20 | Transport_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Transport_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Travel_for_all_purposes_including_education_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Travel_for_all_purposes_including_education_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 63 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_import_and_export_quantity_index_a () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 50 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Automotive_vehicles_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Automotive_vehicles_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Capital_goods_except_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Capital_goods_except_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Charges_for_the_use_of_intellectual_property_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Charges_for_the_use_of_intellectual_property_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Civilian_aircraft_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Civilian_aircraft_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Computers_peripherals_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Computers_peripherals_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Consumer_goods_except_food_and_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Consumer_goods_except_food_and_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 40 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Durable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Durable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Durable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Exports_of_agricultural_goods4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 51 | Exports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Exports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 54 | Exports_of_nonagricultural_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 52 | Exports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Exports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Foods_feeds_and_beverages_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Foods_feeds_and_beverages_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Government_goods_and_services_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Government_goods_and_services_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | Imports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Imports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Imports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 56 | Imports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 57 | Imports_of_nonpetroleum_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Imports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Industrial_supplies_and_materials_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Industrial_supplies_and_materials_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 59 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 41 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Nondurable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Nondurable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Nondurable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Nondurable_goods_excluding_petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Nondurable_goods_excluding_petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 62 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 18 | Other2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Other_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Other_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Other_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Other_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Other_5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Other_business_services3_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Other_business_services3_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 60 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | Petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 61 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 58 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 20 | Transport_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Transport_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Travel_for_all_purposes_including_education_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Travel_for_all_purposes_including_education_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 63 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_import_and_export_quantity_index_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 50 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Automotive_vehicles_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Automotive_vehicles_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Capital_goods_except_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Capital_goods_except_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Charges_for_the_use_of_intellectual_property_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Charges_for_the_use_of_intellectual_property_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Civilian_aircraft_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Civilian_aircraft_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Computers_peripherals_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Computers_peripherals_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Consumer_goods_except_food_and_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Consumer_goods_except_food_and_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 40 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Durable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Durable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Durable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Exports_of_agricultural_goods4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 51 | Exports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Exports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 54 | Exports_of_nonagricultural_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 52 | Exports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Exports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Foods_feeds_and_beverages_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Foods_feeds_and_beverages_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Government_goods_and_services_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Government_goods_and_services_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | Imports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Imports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Imports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 56 | Imports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 57 | Imports_of_nonpetroleum_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Imports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Industrial_supplies_and_materials_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Industrial_supplies_and_materials_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 59 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 41 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Nondurable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Nondurable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Nondurable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Nondurable_goods_excluding_petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Nondurable_goods_excluding_petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 62 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 18 | Other2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Other_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Other_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Other_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Other_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Other_5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Other_business_services3_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Other_business_services3_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 60 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | Petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 61 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 58 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 20 | Transport_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Transport_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Travel_for_all_purposes_including_education_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Travel_for_all_purposes_including_education_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 63 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_import_export_index () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | Agricultural_exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | All_exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | All_imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 3 | Fuel_imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 7 | Nonagricultural_exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Nonfuel_imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 10 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 11 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 8 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 13 | Updatetime | b'datetime' | YES | bytearray(b'') |



### s01_us_import_export_index_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | Agricultural_exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | All_exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | All_imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 3 | Fuel_imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Nonagricultural_exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Nonfuel_imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 10 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 11 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 8 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 13 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_import_price () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | All_imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Automotive_vehicles_parts_and_engines | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Capital_goods | b'varchar(255)' | YES | bytearray(b'') |
| 7 | Consumer_goods_excluding_automotives | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 3 | Foods_feeds_and_beverages | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Industrial_supplies_and_materials | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 12 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 10 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 11 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 8 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 13 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_industrial_value_added_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 87 | Accommodation | b'decimal(18,4)' | YES | bytearray(b'') |
| 86 | Accommodation_and_food_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 99 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 73 | Administrative_and_support_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 72 | Administrative_and_waste_management_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Agriculture_forestry_fishing_and_hunting | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Air_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 78 | Ambulatory_health_care_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 85 | Amusements_gambling_and_recreation_industries | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Apparel_and_leather_and_allied_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 83 | Arts_entertainment_and_recreation | b'decimal(18,4)' | YES | bytearray(b'') |
| 82 | Arts_entertainment_recreation_accommodation_and_food_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Broadcasting_and_telecommunications | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Chemical_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Computer_and_electronic_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 69 | Computer_systems_design_and_related_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Construction | b'decimal(18,4)' | YES | bytearray(b'') |
| 54 | D_p_i_p_a_o_i_s | b'decimal(18,4)' | YES | bytearray(b'Data_processing_internet_publishing_and_other_information_services') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 14 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 76 | Educational_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 75 | Educational_services_health_care_and_social_assistance | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Electrical_equipment_appliances_and_components | b'decimal(18,4)' | YES | bytearray(b'') |
| 57 | F_R_b_c_i_a_r_a | b'decimal(18,4)' | YES | bytearray(b'Federal_Reserve_banks_credit_intermediation_and_related_activities') |
| 18 | Fabricated_metal_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Farms | b'decimal(18,4)' | YES | bytearray(b'') |
| 91 | Federal | b'decimal(18,4)' | YES | bytearray(b'') |
| 56 | Finance_and_insurance | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | Finance_insurance_real_estate_rental_and_leasing | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Food_and_beverage_and_tobacco_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Food_and_beverage_stores | b'decimal(18,4)' | YES | bytearray(b'') |
| 88 | Food_services_and_drinking_places | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Forestry_fishing_and_related_activities | b'decimal(18,4)' | YES | bytearray(b'') |
| 60 | Funds_trusts_and_other_financial_vehicles | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Furniture_and_related_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 92 | General_government_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 97 | General_government_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | General_merchandise_stores | b'decimal(18,4)' | YES | bytearray(b'') |
| 90 | Government | b'decimal(18,4)' | YES | bytearray(b'') |
| 95 | Government_enterprises_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 98 | Government_enterprises_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 77 | Health_care_and_social_assistance | b'decimal(18,4)' | YES | bytearray(b'') |
| 79 | Hospitals | b'decimal(18,4)' | YES | bytearray(b'') |
| 63 | Housing | b'decimal(18,4)' | YES | bytearray(b'') |
| 50 | Information | b'decimal(18,4)' | YES | bytearray(b'') |
| 102 | Information_communications_technology_producing_industries_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 59 | Insurance_carriers_and_related_activities | b'decimal(18,4)' | YES | bytearray(b'') |
| 68 | Legal_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Machinery | b'decimal(18,4)' | YES | bytearray(b'') |
| 71 | Management_of_companies_and_enterprises | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Manufacturing | b'decimal(18,4)' | YES | bytearray(b'') |
| 104 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Mining | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Mining_except_oil_and_gas | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Miscellaneous_manufacturing | b'decimal(18,4)' | YES | bytearray(b'') |
| 70 | Miscellaneous_professional_scientific_and_technical_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 52 | Motion_picture_and_sound_recording_industries | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Motor_vehicle_and_parts_dealers | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Motor_vehicles_bodies_and_trailers_and_parts | b'decimal(18,4)' | YES | bytearray(b'') |
| 93 | National_defense | b'decimal(18,4)' | YES | bytearray(b'') |
| 94 | Nondefense | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Nonmetallic_mineral_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 80 | Nursing_and_residential_care_facilities | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Oil_and_gas_extraction | b'decimal(18,4)' | YES | bytearray(b'') |
| 107 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 64 | Other_real_estate | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Other_retail | b'decimal(18,4)' | YES | bytearray(b'') |
| 89 | Other_services_except_government | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Other_transportation_and_support_activities | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Other_transportation_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Paper_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 84 | Performing_arts_spectator_sports_museums_and_related_activities | b'decimal(18,4)' | YES | bytearray(b'') |
| 105 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 32 | Petroleum_and_coal_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Pipeline_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Plastics_and_rubber_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Primary_metals | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Printing_and_related_support_activities | b'decimal(18,4)' | YES | bytearray(b'') |
| 100 | Private_goods_producing_industries_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Private_industries | b'decimal(18,4)' | YES | bytearray(b'') |
| 101 | Private_services_producing_industries_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 66 | Professional_and_business_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 67 | Professional_scientific_and_technical_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 51 | Publishing_industries_except_internet_includes_software | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Rail_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 62 | Real_estate | b'decimal(18,4)' | YES | bytearray(b'') |
| 61 | Real_estate_and_rental_and_leasing | b'decimal(18,4)' | YES | bytearray(b'') |
| 65 | Rental_and_leasing_services_and_lessors_of_intangible_assets | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Retail_trade | b'decimal(18,4)' | YES | bytearray(b'') |
| 58 | Securities_commodity_contracts_and_investments | b'decimal(18,4)' | YES | bytearray(b'') |
| 81 | Social_assistance | b'decimal(18,4)' | YES | bytearray(b'') |
| 106 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 103 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 96 | State_and_local | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Support_activities_for_mining | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Textile_mills_and_textile_product_mills | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Transit_and_ground_passenger_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | Transportation_and_warehousing | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Truck_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 108 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 11 | Utilities | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Warehousing_and_storage | b'decimal(18,4)' | YES | bytearray(b'') |
| 74 | Waste_management_and_remediation_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Water_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Wholesale_trade | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Wood_products | b'decimal(18,4)' | YES | bytearray(b'') |



### s01_us_industrial_value_added_y () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 87 | Accommodation | b'decimal(18,4)' | YES | bytearray(b'') |
| 86 | Accommodation_and_food_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 99 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 73 | Administrative_and_support_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 72 | Administrative_and_waste_management_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Agriculture_forestry_fishing_and_hunting | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Air_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 78 | Ambulatory_health_care_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 85 | Amusements_gambling_and_recreation_industries | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Apparel_and_leather_and_allied_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 83 | Arts_entertainment_and_recreation | b'decimal(18,4)' | YES | bytearray(b'') |
| 82 | Arts_entertainment_recreation_accommodation_and_food_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Broadcasting_and_telecommunications | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Chemical_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Computer_and_electronic_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 69 | Computer_systems_design_and_related_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Construction | b'decimal(18,4)' | YES | bytearray(b'') |
| 54 | D_p_i_p_a_o_i_s | b'decimal(18,4)' | YES | bytearray(b'Data_processing_internet_publishing_and_other_information_services') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 14 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 76 | Educational_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 75 | Educational_services_health_care_and_social_assistance | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Electrical_equipment_appliances_and_components | b'decimal(18,4)' | YES | bytearray(b'') |
| 57 | F_R_b_c_i_a_r_a | b'decimal(18,4)' | YES | bytearray(b'Federal_Reserve_banks_credit_intermediation_and_related_activities') |
| 18 | Fabricated_metal_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Farms | b'decimal(18,4)' | YES | bytearray(b'') |
| 91 | Federal | b'decimal(18,4)' | YES | bytearray(b'') |
| 56 | Finance_and_insurance | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | Finance_insurance_real_estate_rental_and_leasing | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Food_and_beverage_and_tobacco_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Food_and_beverage_stores | b'decimal(18,4)' | YES | bytearray(b'') |
| 88 | Food_services_and_drinking_places | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Forestry_fishing_and_related_activities | b'decimal(18,4)' | YES | bytearray(b'') |
| 60 | Funds_trusts_and_other_financial_vehicles | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Furniture_and_related_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 92 | General_government_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 97 | General_government_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | General_merchandise_stores | b'decimal(18,4)' | YES | bytearray(b'') |
| 90 | Government | b'decimal(18,4)' | YES | bytearray(b'') |
| 95 | Government_enterprises_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 98 | Government_enterprises_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 77 | Health_care_and_social_assistance | b'decimal(18,4)' | YES | bytearray(b'') |
| 79 | Hospitals | b'decimal(18,4)' | YES | bytearray(b'') |
| 63 | Housing | b'decimal(18,4)' | YES | bytearray(b'') |
| 50 | Information | b'decimal(18,4)' | YES | bytearray(b'') |
| 102 | Information_communications_technology_producing_industries_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 59 | Insurance_carriers_and_related_activities | b'decimal(18,4)' | YES | bytearray(b'') |
| 68 | Legal_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Machinery | b'decimal(18,4)' | YES | bytearray(b'') |
| 71 | Management_of_companies_and_enterprises | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Manufacturing | b'decimal(18,4)' | YES | bytearray(b'') |
| 104 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Mining | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Mining_except_oil_and_gas | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Miscellaneous_manufacturing | b'decimal(18,4)' | YES | bytearray(b'') |
| 70 | Miscellaneous_professional_scientific_and_technical_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 52 | Motion_picture_and_sound_recording_industries | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Motor_vehicle_and_parts_dealers | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Motor_vehicles_bodies_and_trailers_and_parts | b'decimal(18,4)' | YES | bytearray(b'') |
| 93 | National_defense | b'decimal(18,4)' | YES | bytearray(b'') |
| 94 | Nondefense | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Nonmetallic_mineral_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 80 | Nursing_and_residential_care_facilities | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Oil_and_gas_extraction | b'decimal(18,4)' | YES | bytearray(b'') |
| 107 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 64 | Other_real_estate | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Other_retail | b'decimal(18,4)' | YES | bytearray(b'') |
| 89 | Other_services_except_government | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Other_transportation_and_support_activities | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Other_transportation_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Paper_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 84 | Performing_arts_spectator_sports_museums_and_related_activities | b'decimal(18,4)' | YES | bytearray(b'') |
| 105 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 32 | Petroleum_and_coal_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Pipeline_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Plastics_and_rubber_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Primary_metals | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Printing_and_related_support_activities | b'decimal(18,4)' | YES | bytearray(b'') |
| 100 | Private_goods_producing_industries_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Private_industries | b'decimal(18,4)' | YES | bytearray(b'') |
| 101 | Private_services_producing_industries_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 66 | Professional_and_business_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 67 | Professional_scientific_and_technical_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 51 | Publishing_industries_except_internet_includes_software | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Rail_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 62 | Real_estate | b'decimal(18,4)' | YES | bytearray(b'') |
| 61 | Real_estate_and_rental_and_leasing | b'decimal(18,4)' | YES | bytearray(b'') |
| 65 | Rental_and_leasing_services_and_lessors_of_intangible_assets | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Retail_trade | b'decimal(18,4)' | YES | bytearray(b'') |
| 58 | Securities_commodity_contracts_and_investments | b'decimal(18,4)' | YES | bytearray(b'') |
| 81 | Social_assistance | b'decimal(18,4)' | YES | bytearray(b'') |
| 106 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 103 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 96 | State_and_local | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Support_activities_for_mining | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Textile_mills_and_textile_product_mills | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Transit_and_ground_passenger_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | Transportation_and_warehousing | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Truck_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 108 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 11 | Utilities | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Warehousing_and_storage | b'decimal(18,4)' | YES | bytearray(b'') |
| 74 | Waste_management_and_remediation_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Water_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Wholesale_trade | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Wood_products | b'decimal(18,4)' | YES | bytearray(b'') |



### s01_us_inflation () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | All_items | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | All_items_less_food_and_energy | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Apparel | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Commodities_less_food_and_energy_commodities | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 18 | Education_and_communication | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Electricity | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Energy | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Food | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Food_at_home | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Food_away_from_home | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Gasoline_all_types | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 14 | Medical_care_commodities | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Medical_care_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Natural_gas_piped | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | New_vehicles | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 21 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 15 | Services_less_energy_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Shelter | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 19 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 24 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_internationalpositionnet_yq () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | A_e_f_d_s_o_l_7_8_10_a_11 | b'decimal(18,4)' | YES | bytearray(b'Assets_excluding_financial_derivatives_sum_of_lines_7_8_10_and_11') |
| 8 | By_functional_category_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | By_functional_category_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 9 | Direct_investment_at_market_value_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Direct_investment_at_market_value_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | F_d_o_t_r_g_n_f_v | b'decimal(18,4)' | YES | bytearray(b'Financial_derivatives_other_than_reserves_gross_negative_fair_value') |
| 16 | F_d_o_t_r_g_n_f_v_l_17 | b'decimal(18,4)' | YES | bytearray(b'Financial_derivatives_other_than_reserves_gross_negative_fair_value_line_17') |
| 11 | F_d_o_t_r_g_p_f_v | b'decimal(18,4)' | YES | bytearray(b'Financial_derivatives_other_than_reserves_gross_positive_fair_value') |
| 7 | F_d_o_t_r_g_p_f_v_l_9 | b'decimal(18,4)' | YES | bytearray(b'Financial_derivatives_other_than_reserves_gross_positive_fair_value_line_9') |
| 4 | F_d_o_t_r_n_l_6_l_l_14 | b'decimal(18,4)' | YES | bytearray(b'Financial_derivatives_other_than_reserves_net_line_6_less_line_14') |
| 15 | L_e_f_d_s_o_l_15_16_a_18 | b'decimal(18,4)' | YES | bytearray(b'Liabilities_excluding_financial_derivatives_sum_of_lines_15_16_and_18') |
| 23 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 3 | N_i_i_p_e_f_d_l_5_l_l_13 | b'decimal(18,4)' | YES | bytearray(b'Net_international_investment_position_excluding_financial_derivatives_line_5_less_line_13') |
| 26 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 12 | Other_investment_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Other_investment_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 10 | Portfolio_investment_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Portfolio_investment_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Reserve_assets | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 22 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 5 | U_S_assets | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | U_S_liabilities | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | U_S_n_i_i_p_l_4_l_l_12 | b'decimal(18,4)' | YES | bytearray(b'U_S_net_international_investment_position_line_4_less_line_12') |
| 27 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_jolt_job_openings () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 2 | Job_Openings | b'int(8)' | YES | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_m3_durable_goods_inventory_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | value | b'decimal(18,4)' | YES | bytearray(b'') |



### s01_us_m3_durable_goods_new_order_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | value | b'decimal(18,4)' | YES | bytearray(b'') |



### s01_us_m3_durable_goods_shipment_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | value | b'decimal(18,4)' | YES | bytearray(b'') |



### s01_us_m3inventories_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | value | b'decimal(18,4)' | YES | bytearray(b'') |



### s01_us_m3neworders_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | value | b'decimal(18,4)' | YES | bytearray(b'') |



### s01_us_m3value_of_shipment_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | value | b'decimal(18,4)' | YES | bytearray(b'') |



### s01_us_michigan_consumer_sentiment () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 2 | Michigan_University_Consumer_Sentiment | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_nahb_wells_fargo_national_hmi_components_history () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | category | b'varchar(100)' | NO | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 5 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 8 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 6 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 7 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 4 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 9 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 3 | value | b'decimal(18,4)' | YES | bytearray(b'') |



### s01_us_nahb_wells_fargo_national_hmi_history () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | value | b'decimal(18,4)' | YES | bytearray(b'') |



### s01_us_nonfarm_payrolls_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 2 | Nonfarm_payrolls_change | b'int(8)' | YES | bytearray(b'') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_nrp () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 30 | Change_in_Banks_Own_Net_Dollar_denom_Liabs | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Domes_LT_Secur_Purch_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Foreign_Bonds_Purch_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Foreign_Equity_Purch_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Foreign_LT_Secur_Purch_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Gross_Foreign_Purch_Foreign_LT_Secur_from_US | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_Foreign_Purch_of_Domes_US_LT_Secur | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Gross_Foreign_Sales_Foreign_LT_Secur_to_US | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Gross_Foreign_Sales_of_Domes_US_LT_Secur | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Increase_in_ForeignHoldings_of_Dollardenom_ST_US_S_O_C_L | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 31 | Monthly_Net_TIC_Flows | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Net_Foreign_Acquis_of_LT_Secur | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Net_LT_Secur_ransac | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Official_Corp_Bonds_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Official_Equity_Net | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Official_Gov_t_Agency_Bonds_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Official_net_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Official_net_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Official_net_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Official_net_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Official_Treas_Bonds_Notes_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 21 | Other_Acquis_LT_Secur_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Other_Negot_Instr_Select_Other_Liabs | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 8 | Private_Corp_Bonds_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Private_Equity_Net | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Private_Gov_t_Agency_Bonds_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Private_net_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Private_net_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Private_net_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Private_net_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Private_Treas_Bonds_Notes_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 34 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 39 | Updatetime | b'datetime' | YES | bytearray(b'') |
| 24 | US_Treas_Bills | b'decimal(18,4)' | YES | bytearray(b'') |



### s01_us_permits_cust () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | category | b'varchar(20)' | NO | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | In_structures_with_1unit | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | In_structures_with_2_to_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | In_structures_with_5units | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 19 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 17 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 10 | RegionMidwest_1unit | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | RegionMidwestTotal | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | RegionNortheast_1unit | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | RegionNortheastTotal | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | RegionSouth_1unit | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | RegionSouthTotal | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | RegionWest_1unit | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | RegionWestTotal | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 15 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 3 | Total | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Updatetime | b'datetime' | YES | bytearray(b'') |



### s01_us_personal_income_and_expenses_monthly () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 37 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Chained_dollars | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Compensation_of_employees | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Current_dollars | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 39 | Disposable_personal_income | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | E_c_f_e_p_a_i_f | b'decimal(18,4)' | YES | bytearray(b'Employer contributions for employee pension and insurance funds1') |
| 9 | Employer_contributions_for_government_social_insurance | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Equals_Disposable_personal_income | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Equals_Personal_saving | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Farm | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Government | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Government_social_benefits_to_persons | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Less_Contributions_for_government_social_insurance_domestic | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Less_Personal_current_taxes | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Less_Personal_outlays | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 21 | Medicaid | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Medicare3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Nonfarm | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 24 | Other | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Other_current_transfer_receipts_from_business_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | P_i_e_c_t_r_b_o_c_2_d | b'decimal(18,4)' | YES | bytearray(b'Personal_income_excluding_current_transfer_receipts_billions_of_chained_2009_dollars5') |
| 10 | P_i_w_i_v_a_c_c_a | b'decimal(18,4)' | YES | bytearray(b'Proprietors_income_with_inventory_valuation_and_capital_consumption_adjustments') |
| 41 | Per_capita | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 30 | Personal_consumption_expenditures | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Personal_current_transfer_payments | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Personal_current_transfer_receipts | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Personal_dividend_income | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Personal_income | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Personal_income_receipts_on_assets | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Personal_interest_income | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Personal_interest_payments4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Personal_saving_as_a_percentage_of_disposable_personal_income | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Population_midperiod_thousands_6 | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Private_industries | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Rental_income_of_persons_with_capital_consumption_adjustment | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Social_security2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 45 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 7 | Supplements_to_wages_and_salaries | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | To_government | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | To_the_rest_of_the_world_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Total_billions_of_chained_dollars5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Unemployment_insurance | b'decimal(18,4)' | YES | bytearray(b'') |
| 50 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 23 | Veterans_benefits | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Wages_and_salaries | b'decimal(18,4)' | YES | bytearray(b'') |



### s01_us_policy_rate_d () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 5 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 8 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 6 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 2 | RESBME_ND | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | RESBMS_ND | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 4 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 9 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_ppi_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 12 | category | b'varchar(30)' | YES | bytearray(b'\xe5\x88\x86\xe7\xb1\xbb') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 6 | Energy | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Foods | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Goods_less_foods_and_energy | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 17 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 15 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | Services | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Services_less_trade_transportation_and_warehousing | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 13 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 2 | Total | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Total_less_foods_energy_and_trade_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Trade | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Transportation_and_warehousing | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_ppi_y () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 12 | category | b'varchar(30)' | YES | bytearray(b'\xe5\x88\x86\xe7\xb1\xbb') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 6 | Energy | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Foods | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Goods_less_foods_and_energy | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 17 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 15 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | Services | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Services_less_trade_transportation_and_warehousing | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 13 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 2 | Total | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Total_less_foods_energy_and_trade_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Trade | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Transportation_and_warehousing | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_price_index_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 15 | Change_in_private_inventories | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 5 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Federal | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Fixed_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Government_consumption_expenditures_and_gross_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Gross_private_domestic_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Intellectual_property_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 25 | National_defense | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Net_exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Nondefense | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Nonresidential | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 30 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 3 | Personal_consumption_expenditures | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Residential | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Services | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Services_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Services_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 28 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 27 | State_and_local | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Structures | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_price_index_y () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 15 | Change_in_private_inventories | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 5 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Federal | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Fixed_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Government_consumption_expenditures_and_gross_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Gross_private_domestic_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Intellectual_property_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 25 | National_defense | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Net_exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Nondefense | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Nonresidential | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 30 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 3 | Personal_consumption_expenditures | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Residential | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Services | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Services_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Services_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 28 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 27 | State_and_local | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Structures | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_r539cy () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | Continued_Claims_NSA | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Continued_Claims_SA | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Continued_Claims_SA_4_Week | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Continued_Claims_SF | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Covered_Employment | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 2 | Initial_Claims_NSA | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Initial_Claims_SA | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Initial_Claims_SA_4_Week | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Initial_Claims_SF | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | IUR_NSA | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | IUR_SA | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 17 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 15 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 16 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 13 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 18 | Updatetime | b'datetime' | YES | bytearray(b'') |



### s01_us_realgdp_a () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 43 | Change_in_private_inventories | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Clothing_and_footwear | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Computers_and_peripheral_equipment4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 56 | Consumption_expenditures_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 59 | Consumption_expenditures_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 62 | Consumption_expenditures_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 5 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | Entertainment_literary_and_artistic_originals | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | F_c_e_o_n_i_s_h_N | b'decimal(18,4)' | YES | bytearray(b'Final_consumption_expenditures_of_nonprofit_institutions_serving_households_NPISHs1') |
| 44 | Farm | b'decimal(18,4)' | YES | bytearray(b'') |
| 54 | Federal | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Financial_services_and_insurance | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Fixed_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Food_and_beverages_purchased_for_off_premises_consumption | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Food_services_and_accommodations | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Furnishings_and_durable_household_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Gasoline_and_other_energy_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 51 | Goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Government_consumption_expenditures_and_gross_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 57 | Gross_investment_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 60 | Gross_investment_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 63 | Gross_investment_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Gross_output_of_nonprofit_institutions2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Gross_private_domestic_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Health_care | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Household_consumption_expenditures_for_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Housing_and_utilities | b'decimal(18,4)' | YES | bytearray(b'') |
| 50 | Imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Industrial_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Information_processing_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Intellectual_property_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | L_R_f_s_o_g_a_s_b_n_i | b'decimal(18,4)' | YES | bytearray(b'Less_Receipts_from_sales_of_goods_and_services_by_nonprofit_institutions3') |
| 66 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 6 | Motor_vehicles_and_parts | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | National_defense | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Net_exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 58 | Nondefense | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Nonfarm | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Nonresidential | b'decimal(18,4)' | YES | bytearray(b'') |
| 69 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 34 | Other | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Other_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Other_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Other_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Other_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 67 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 3 | Personal_consumption_expenditures | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Recreation_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Recreational_goods_and_vehicles | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Research_and_development6 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Residential | b'decimal(18,4)' | YES | bytearray(b'') |
| 64 | Residual | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Services | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Services_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 52 | Services_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Software5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 68 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 65 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 61 | State_and_local | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Structures | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Transportation_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Transportation_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 70 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_realgdp_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 43 | Change_in_private_inventories | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Clothing_and_footwear | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Computers_and_peripheral_equipment4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 56 | Consumption_expenditures_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 59 | Consumption_expenditures_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 62 | Consumption_expenditures_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 5 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | Entertainment_literary_and_artistic_originals | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | F_c_e_o_n_i_s_h_N | b'decimal(18,4)' | YES | bytearray(b'Final_consumption_expenditures_of_nonprofit_institutions_serving_households_NPISHs1') |
| 44 | Farm | b'decimal(18,4)' | YES | bytearray(b'') |
| 54 | Federal | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Financial_services_and_insurance | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Fixed_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Food_and_beverages_purchased_for_off_premises_consumption | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Food_services_and_accommodations | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Furnishings_and_durable_household_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Gasoline_and_other_energy_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 51 | Goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Government_consumption_expenditures_and_gross_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 57 | Gross_investment_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 60 | Gross_investment_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 63 | Gross_investment_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Gross_output_of_nonprofit_institutions2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Gross_private_domestic_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Health_care | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Household_consumption_expenditures_for_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Housing_and_utilities | b'decimal(18,4)' | YES | bytearray(b'') |
| 50 | Imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Industrial_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Information_processing_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Intellectual_property_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | L_R_f_s_o_g_a_s_b_n_i | b'decimal(18,4)' | YES | bytearray(b'Less_Receipts_from_sales_of_goods_and_services_by_nonprofit_institutions3') |
| 66 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 6 | Motor_vehicles_and_parts | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | National_defense | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Net_exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 58 | Nondefense | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Nonfarm | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Nonresidential | b'decimal(18,4)' | YES | bytearray(b'') |
| 69 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 34 | Other | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Other_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Other_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Other_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Other_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 67 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 3 | Personal_consumption_expenditures | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Recreation_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Recreational_goods_and_vehicles | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Research_and_development6 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Residential | b'decimal(18,4)' | YES | bytearray(b'') |
| 64 | Residual | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Services | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Services_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 52 | Services_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Software5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 68 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 65 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 61 | State_and_local | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Structures | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Transportation_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Transportation_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 70 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_retail_sales_ym () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 68 | ADJUSTED_2 | b'decimal(18,4)' | YES | bytearray(b'ADJUSTED(2)') |
| 54 | All_other_gen_merchandise_stores_1 | b'decimal(18,4)' | YES | bytearray(b'All other gen. merchandise stores') |
| 101 | All_other_gen_merchandise_stores_2 | b'decimal(18,4)' | YES | bytearray(b'All other gen. merchandise stores') |
| 21 | All_other_home_furnishings_stores_1 | b'decimal(18,4)' | YES | bytearray(b'All other home furnishings stores') |
| 11 | Automobile_and_other_motor_vehicle_dealers_1 | b'decimal(18,4)' | YES | bytearray(b'Automobile and other motor vehicle dealers') |
| 77 | Automobile_and_other_motor_vehicle_dealers_2 | b'decimal(18,4)' | YES | bytearray(b'Automobile and other motor vehicle dealers') |
| 12 | Automobile_dealers_1 | b'decimal(18,4)' | YES | bytearray(b'Automobile dealers') |
| 15 | Automotive_parts_acc_1and_tire_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Automotive parts, acc., and tire stores') |
| 78 | Automotive_parts_acc_and_tire_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Automotive parts, acc., and tire stores') |
| 32 | Beer_wine_and_liquor_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Beer, wine, and liquor stores') |
| 86 | Beer_wine_and_liquor_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Beer, wine and liquor stores') |
| 47 | Book_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Book stores') |
| 25 | Building_mat_and_garden_equip_and_supplies_dealers_1 | b'decimal(18,4)' | YES | bytearray(b'Building mat. and garden equip. and supplies dealers') |
| 82 | Building_mat_and_garden_equip_and_supplies_dealers_2 | b'decimal(18,4)' | YES | bytearray(b'Building mat. and garden equip. and supplies dealers') |
| 26 | Building_mat_and_supplies_dealers_1 | b'decimal(18,4)' | YES | bytearray(b'Building mat. and supplies dealers') |
| 83 | Building_mat_and_supplies_dealers_2 | b'decimal(18,4)' | YES | bytearray(b'Building mat. and supplies dealers') |
| 36 | Clothing_and_clothing_access_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Clothing and clothing access. stores') |
| 90 | Clothing_and_clothing_access_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Clothing and clothing access. stores') |
| 37 | Clothing_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Clothing stores') |
| 91 | Clothing_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Clothing stores') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 49 | Department_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Department stores') |
| 98 | Department_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Department stores') |
| 50 | Department_stores_excl_discount_department_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Department stores(excl. discount department stores)') |
| 51 | Discount_dept_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Discount dept. stores') |
| 64 | Drinking_places_1 | b'decimal(18,4)' | YES | bytearray(b'Drinking places') |
| 61 | Electronic_shopping_and_mail_order_houses_1 | b'decimal(18,4)' | YES | bytearray(b'Electronic shopping and mail-order houses') |
| 104 | Electronic_shopping_and_mail_order_houses_2 | b'decimal(18,4)' | YES | bytearray(b'Electronic shopping and mail order houses') |
| 22 | Electronics_and_appliance_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Electronics and appliance stores') |
| 81 | Electronics_and_appliance_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Electronics and appliance stores') |
| 24 | Electronics_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Electronics stores') |
| 40 | Family_clothing_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Family clothing stores') |
| 20 | Floor_covering_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Floor covering stores') |
| 29 | Food_and_beverage_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Food and beverage stores') |
| 84 | Food_and_beverage_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Food and beverage stores') |
| 63 | Food_services_and_drinking_places_1 | b'decimal(18,4)' | YES | bytearray(b'Food services and drinking places') |
| 106 | Food_services_and_drinking_places_2 | b'decimal(18,4)' | YES | bytearray(b'Food services and drinking places') |
| 62 | Fuel_dealers_1 | b'decimal(18,4)' | YES | bytearray(b'Fuel dealers') |
| 105 | Fuel_dealers_2 | b'decimal(18,4)' | YES | bytearray(b'Fuel dealers') |
| 66 | Full_service_restaurants_1 | b'decimal(18,4)' | YES | bytearray(b'Full service restaurants') |
| 17 | Furniture_and_home_furnishings_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Furniture and home furnishings stores') |
| 80 | Furniture_and_home_furnishings_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Furniture and home furnishings stores') |
| 16 | Furniture_home_furn_electronics_and_appliance_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Furniture, home furn, electronics, and appliance stores') |
| 79 | Furniture_home_furn_electronics_and_appliance_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Furniture, home furn, electronics, and appliance stores') |
| 18 | Furniture_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Furniture stores') |
| 9 | GAFO_1 | b'decimal(18,4)' | YES | bytearray(b'GAFO(1)') |
| 75 | GAFO_2 | b'decimal(18,4)' | YES | bytearray(b'GAFO(1)') |
| 35 | Gasoline_stations_1 | b'decimal(18,4)' | YES | bytearray(b'Gasoline stations') |
| 89 | Gasoline_stations_2 | b'decimal(18,4)' | YES | bytearray(b'Gasoline stations') |
| 48 | General_merchandise_stores_1 | b'decimal(18,4)' | YES | bytearray(b'General merchandise stores') |
| 97 | General_merchandise_stores_2 | b'decimal(18,4)' | YES | bytearray(b'General merchandise stores') |
| 58 | Gift_novelty_and_souvenir_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Gift, novelty, and souvenir stores') |
| 30 | Grocery_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Grocery stores') |
| 85 | Grocery_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Grocery stores') |
| 28 | Hardware_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Hardware stores') |
| 33 | Health_and_personal_care_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Health and personal care stores') |
| 87 | Health_and_personal_care_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Health and personal care stores') |
| 46 | Hobby_toy_and_game_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Hobby, toy, and game stores') |
| 19 | Home_furnishings_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Home furnishings stores') |
| 23 | Household_appliance_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Household appliance stores') |
| 43 | Jewelry_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Jewelry stores') |
| 95 | Jewelry_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Jewelry stores') |
| 67 | Limited_service_eating_places_1 | b'decimal(18,4)' | YES | bytearray(b'Limited service eating places') |
| 108 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 38 | Mens_clothing_stores_1 | b'decimal(18,4)' | YES | bytearray(b"Men\'s clothing stores") |
| 92 | Mens_clothing_stores_2 | b'decimal(18,4)' | YES | bytearray(b"Men\'s clothing stores") |
| 55 | Miscellaneous_store_retailers_1 | b'decimal(18,4)' | YES | bytearray(b'Miscellaneous store retailers') |
| 102 | Miscellaneous_stores_retailers_2 | b'decimal(18,4)' | YES | bytearray(b'Miscellaneous stores retailers') |
| 10 | Motor_vehicle_and_parts_dealers | b'decimal(18,4)' | YES | bytearray(b'Motor vehicle and parts dealers') |
| 76 | Motor_vehicle_and_parts_dealers_2 | b'decimal(18,4)' | YES | bytearray(b'Motor vehicle and parts dealers') |
| 13 | New_car_dealers_1 | b'decimal(18,4)' | YES | bytearray(b'New car dealers') |
| 60 | Nonstore_retailers_1 | b'decimal(18,4)' | YES | bytearray(b'Nonstore retailers') |
| 103 | Nonstore_retailers_2 | b'decimal(18,4)' | YES | bytearray(b'Nonstore retailers') |
| 2 | NOT_ADJUSTED | b'decimal(18,4)' | YES | bytearray(b'NOT ADJUSTED') |
| 57 | Office_supplies_and_stationery_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Office supplies and stationery stores') |
| 56 | Office_supplies_stationery_and_gift_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Office supplies, stationery, and gift stores') |
| 111 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 41 | Other_clothing_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Other clothing stores') |
| 52 | Other_general_merchandise_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Other general merchandise stores') |
| 99 | Other_general_merchandise_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Other general merchandise stores') |
| 27 | Paint_and_wallpaper_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Paint and wallpaper stores') |
| 109 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 34 | Pharmacies_and_drug_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Pharmacies and drug stores') |
| 88 | Pharmacies_and_drug_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Pharmacies and drug stores') |
| 72 | R_s_and_f_s_e_motor_v_and_parts_and_gasoline_s_2 | b'decimal(18,4)' | YES | bytearray(b'Retail sales and food services excl motor vehicle and parts and gasoline stations') |
| 71 | R_s_and_f_s_excl_gasoline_stations_2 | b'decimal(18,4)' | YES | bytearray(b'Retail sales and food services excl gasoline stations') |
| 6 | R_s_and_f_s_excl_motor_v_and_parts_and_gasoline_s_1 | b'decimal(18,4)' | YES | bytearray(b'Retail sales and food services excl motor vehicle and parts and gasoline stations') |
| 4 | R_s_and_f_s_excl_motor_vehicle_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'Retail sales and food services excl motor vehicle and parts') |
| 70 | R_s_and_f_s_excl_motor_vehicle_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'Retail sales and food services excl motor vehicle and parts') |
| 8 | R_s_t_excl_motor_vehicle_and_parts_dealers | b'decimal(18,4)' | YES | bytearray(b'Retail sales, total (excl. motor vehicle and parts dealers)') |
| 74 | R_s_total_excl_motor_vehicle_and_parts_dealers_2 | b'decimal(18,4)' | YES | bytearray(b'Retail sales, total (excl. motor vehicle and parts dealers)') |
| 65 | Restaurants_and_other_eating_places_1 | b'decimal(18,4)' | YES | bytearray(b'Restaurants and other eating places') |
| 3 | Retail_and_food_services_sales_total_1 | b'decimal(18,4)' | YES | bytearray(b'Retail and food services sales, total') |
| 69 | Retail_and_food_services_sales_total_2 | b'decimal(18,4)' | YES | bytearray(b'Retail and food services sales, total') |
| 5 | Retail_sales_and_food_services_excl_gasoline_stations_1 | b'decimal(18,4)' | YES | bytearray(b'Retail sales and food services excl gasoline stations') |
| 7 | Retail_sales_total | b'decimal(18,4)' | YES | bytearray(b'Retail sales, total') |
| 73 | Retail_sales_total_2 | b'decimal(18,4)' | YES | bytearray(b'Retail sales, total') |
| 42 | Shoe_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Shoe stores') |
| 94 | Shoe_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Shoe stores') |
| 110 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 107 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 44 | Sporting_goods_hobby_musical_instrument_and_book_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Sporting goods, hobby, musical instrument, and book stores') |
| 96 | Sporting_goods_hobby_musical_instrument_and_book_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Sporting goods, hobby, musical instrument, and book stores') |
| 45 | Sporting_goods_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Sporting goods stores') |
| 31 | Supermarkets_and_other_grocery_except_convenience_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Supermarkets and other grocery (except convenience) stores') |
| 112 | Updatetime | b'datetime' | YES | bytearray(b'') |
| 14 | Used_car_dealers_1 | b'decimal(18,4)' | YES | bytearray(b'Used car dealers') |
| 59 | Used_merchandise_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Used merchandise stores') |
| 53 | Warehouse_clubs_and_superstores_1 | b'decimal(18,4)' | YES | bytearray(b'Warehouse clubs and superstores') |
| 100 | Warehouse_clubs_and_superstores_2 | b'decimal(18,4)' | YES | bytearray(b'Warehouse clubs and superstores') |
| 39 | Womens_clothing_stores_1 | b'decimal(18,4)' | YES | bytearray(b"Women\'s clothing stores") |
| 93 | Womens_clothing_stores_2 | b'decimal(18,4)' | YES | bytearray(b"Women\'s clothing stores") |



### s01_us_stage_cust () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | category | b'varchar(20)' | NO | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 10 | For_Sale_at_end_of_period_Completed | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | For_Sale_at_end_of_period_Median_Numberof_monthsfor_sale | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | For_Sale_at_end_of_period_NotStarted | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | For_Sale_at_end_of_period_Total | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | For_Sale_at_end_of_period_UnderConstruction | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 16 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 14 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 6 | Sold_during_period_Competed | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Sold_during_period_NotStarted | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Sold_during_period_Total | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Sold_during_period_UnderConstruction | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 12 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 17 | Updatetime | b'datetime' | YES | bytearray(b'') |



### s01_us_underlying_inflation_gauge_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | CPI_inflation | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 6 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 9 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 5 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 2 | UIG_Full_data_set_measure | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | UIG_Prices_only_measure | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_us_unemployment_rate_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 2 | Unemployment_rate | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s01_user_comment () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | date | b'datetime(6)' | NO | bytearray(b'') |
| 5 | file | b'varchar(200)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 3 | usercomment | b'longtext' | NO | bytearray(b'') |
| 2 | username | b'varchar(100)' | NO | bytearray(b'') |



### s01_user_out_company () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 5 | invited_code | b'varchar(100)' | NO | bytearray(b'') |
| 7 | power_level | b'varchar(3)' | NO | bytearray(b'') |
| 6 | powerOff | b'datetime(6)' | NO | bytearray(b'') |
| 4 | userId | b'int(11)' | NO | bytearray(b'') |
| 3 | userinfo | b'varchar(100)' | NO | bytearray(b'') |
| 2 | username | b'varchar(100)' | NO | bytearray(b'') |



### s01_user_sycapital_user () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 13 | creat_date | b'datetime(6)' | NO | bytearray(b'') |
| 9 | Email | b'varchar(30)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 6 | invite_code | b'varchar(100)' | NO | bytearray(b'') |
| 7 | invited_code | b'varchar(100)' | NO | bytearray(b'') |
| 11 | Job | b'varchar(30)' | NO | bytearray(b'') |
| 10 | PartOf | b'varchar(30)' | NO | bytearray(b'') |
| 4 | password | b'varchar(25)' | NO | bytearray(b'') |
| 8 | PhoneNum | b'varchar(13)' | NO | bytearray(b'') |
| 12 | power_level | b'varchar(100)' | NO | bytearray(b'') |
| 14 | up_date | b'datetime(6)' | NO | bytearray(b'') |
| 2 | user | b'varchar(10)' | NO | bytearray(b'') |
| 5 | user_ID | b'int(11)' | NO | bytearray(b'') |
| 3 | username | b'varchar(10)' | NO | bytearray(b'') |



### s01_user_user_session () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 3 | Session_ID | b'varchar(50)' | NO | bytearray(b'') |
| 4 | UpDate | b'datetime(6)' | NO | bytearray(b'') |
| 2 | UserName | b'varchar(10)' | NO | bytearray(b'') |



### s01_yanbao_yanbao () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | author | b'varchar(10)' | NO | bytearray(b'') |
| 8 | biaoqian | b'varchar(50)' | NO | bytearray(b'') |
| 3 | date_time | b'datetime(6)' | NO | bytearray(b'') |
| 4 | fileName | b'varchar(50)' | NO | bytearray(b'') |
| 5 | filePath | b'varchar(100)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 9 | level | b'varchar(20)' | NO | bytearray(b'') |
| 10 | page | b'int(11)' | NO | bytearray(b'') |
| 6 | refer | b'varchar(50)' | NO | bytearray(b'') |
| 2 | title | b'varchar(200)' | NO | bytearray(b'') |
| 11 | update | b'datetime(6)' | NO | bytearray(b'') |



### s02_book () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 8 | Admin | b'varchar(5)' | YES | bytearray(b'\xe5\xae\xa1\xe6\xa0\xb8\xe7\xae\xa1\xe7\x90\x86\xe4\xba\xba') |
| 1 | Book_Name | b'varchar(40)' | YES | bytearray(b'\xe4\xb9\xa6\xe7\xb1\x8d\xe5\x90\x8d\xe7\xa7\xb0') |
| 2 | Borro_Time | b'datetime' | YES | bytearray(b'\xe5\x80\x9f\xe9\x98\x85\xe6\x97\xb6\xe9\x97\xb4') |
| 3 | Borrower | b'varchar(5)' | YES | bytearray(b'\xe5\x80\x9f\xe9\x98\x85\xe4\xba\xba') |
| 7 | ReturnThePeo | b'varchar(255)' | YES | bytearray(b'\xe5\xbd\x92\xe8\xbf\x98\xe4\xba\xba') |
| 6 | ReturnTime | b'datetime' | YES | bytearray(b'\xe5\xbd\x92\xe8\xbf\x98\xe6\x97\xb6\xe9\x97\xb4') |
| 4 | Subte_Time | b'datetime' | YES | bytearray(b'\xe8\xbd\xac\xe5\x80\x9f\xe6\x97\xb6\xe9\x97\xb4') |
| 5 | Subtenant | b'varchar(5)' | YES | bytearray(b'\xe8\xbd\xac\xe5\x80\x9f\xe4\xba\xba') |



### s02_cn_fut_positionranking () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | BBTicker | b'varchar(15)' | YES | bytearray(b'Bloomberg\xe4\xbb\xa3\xe7\xa0\x81') |
| 1 | FutCode | b'varchar(15)' | NO | bytearray(b'\xe5\x90\x88\xe7\xba\xa6\xe4\xbb\xa3\xe7\xa0\x81') |
| 9 | LBroker | b'varchar(20)' | YES | bytearray(b'\xe4\xb9\xb0\xe5\x8d\x95\xe7\x9b\xb8\xe5\x85\xb3\xe6\x9c\x9f\xe8\xb4\xa7\xe5\x85\xac\xe5\x8f\xb8') |
| 10 | LDailyChange | b'int(11)' | YES | bytearray(b'\xe4\xb9\xb0\xe5\x8d\x95\xe9\x87\x8f\xe5\x8f\x98\xe5\x8c\x96') |
| 8 | LongPosition | b'int(11)' | YES | bytearray(b'\xe6\x8c\x81\xe4\xb9\xb0\xe5\x8d\x95\xe9\x87\x8f') |
| 15 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 18 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 16 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 4 | Ranking | b'int(11)' | NO | bytearray(b'\xe6\x8e\x92\xe5\x90\x8d') |
| 12 | SBroker | b'varchar(20)' | YES | bytearray(b'\xe5\x8d\x96\xe5\x8d\x95\xe7\x9b\xb8\xe5\x85\xb3\xe6\x9c\x9f\xe8\xb4\xa7\xe5\x85\xac\xe5\x8f\xb8') |
| 13 | SDailyChange | b'int(11)' | YES | bytearray(b'\xe5\x8d\x96\xe5\x8d\x95\xe5\x8f\x98\xe5\x8c\x96') |
| 11 | ShortPosition | b'int(11)' | YES | bytearray(b'\xe6\x8c\x81\xe5\x8d\x96\xe5\x8d\x95\xe9\x87\x8f') |
| 17 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 14 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 3 | Tradingday | b'datetime' | NO | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe6\x97\xa5') |
| 19 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 5 | VBroker | b'varchar(20)' | YES | bytearray(b'\xe6\x88\x90\xe4\xba\xa4\xe9\x87\x8f\xe7\x9b\xb8\xe5\x85\xb3\xe6\x9c\x9f\xe8\xb4\xa7\xe5\x85\xac\xe5\x8f\xb8') |
| 7 | VDailyChange | b'int(11)' | YES | bytearray(b'\xe6\x88\x90\xe4\xba\xa4\xe9\x87\x8f\xe5\x8f\x98\xe5\x8c\x96') |
| 6 | Volume | b'int(11)' | YES | bytearray(b'\xe6\x88\x90\xe4\xba\xa4\xe9\x87\x8f') |



### s02_cn_fut_positionranking_test () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | BBTicker | b'varchar(15)' | YES | bytearray(b'Bloomberg\xe4\xbb\xa3\xe7\xa0\x81') |
| 1 | FutCode | b'varchar(15)' | NO | bytearray(b'\xe5\x90\x88\xe7\xba\xa6\xe4\xbb\xa3\xe7\xa0\x81') |
| 9 | LBroker | b'varchar(20)' | YES | bytearray(b'\xe4\xb9\xb0\xe5\x8d\x95\xe7\x9b\xb8\xe5\x85\xb3\xe6\x9c\x9f\xe8\xb4\xa7\xe5\x85\xac\xe5\x8f\xb8') |
| 10 | LDailyChange | b'int(11)' | YES | bytearray(b'\xe4\xb9\xb0\xe5\x8d\x95\xe9\x87\x8f\xe5\x8f\x98\xe5\x8c\x96') |
| 8 | LongPosition | b'int(11)' | YES | bytearray(b'\xe6\x8c\x81\xe4\xb9\xb0\xe5\x8d\x95\xe9\x87\x8f') |
| 15 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 18 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 16 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 4 | Ranking | b'int(11)' | NO | bytearray(b'\xe6\x8e\x92\xe5\x90\x8d') |
| 12 | SBroker | b'varchar(20)' | YES | bytearray(b'\xe5\x8d\x96\xe5\x8d\x95\xe7\x9b\xb8\xe5\x85\xb3\xe6\x9c\x9f\xe8\xb4\xa7\xe5\x85\xac\xe5\x8f\xb8') |
| 13 | SDailyChange | b'int(11)' | YES | bytearray(b'\xe5\x8d\x96\xe5\x8d\x95\xe5\x8f\x98\xe5\x8c\x96') |
| 11 | ShortPosition | b'int(11)' | YES | bytearray(b'\xe6\x8c\x81\xe5\x8d\x96\xe5\x8d\x95\xe9\x87\x8f') |
| 17 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 14 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 3 | Tradingday | b'datetime' | NO | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe6\x97\xa5') |
| 19 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 5 | VBroker | b'varchar(20)' | YES | bytearray(b'\xe6\x88\x90\xe4\xba\xa4\xe9\x87\x8f\xe7\x9b\xb8\xe5\x85\xb3\xe6\x9c\x9f\xe8\xb4\xa7\xe5\x85\xac\xe5\x8f\xb8') |
| 7 | VDailyChange | b'int(11)' | YES | bytearray(b'\xe6\x88\x90\xe4\xba\xa4\xe9\x87\x8f\xe5\x8f\x98\xe5\x8c\x96') |
| 6 | Volume | b'int(11)' | YES | bytearray(b'\xe6\x88\x90\xe4\xba\xa4\xe9\x87\x8f') |



### s02_cn_stock_statistical (中国股指统计表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | Asset_Then_Equity | b'decimal(18,4)' | YES | bytearray(b'Asset\xe6\xaf\x94Equity') |
| 18 | Asset_turnover | b'decimal(18,4)' | YES | bytearray(b'\xe8\xb5\x84\xe4\xba\xa7\xe5\x91\xa8\xe8\xbd\xac\xe7\x8e\x87') |
| 13 | Cash_ratio | b'decimal(18,4)' | YES | bytearray(b'\xe7\x8e\xb0\xe9\x87\x91\xe5\x8d\xa0\xe6\xaf\x94') |
| 4 | Classify | b'varchar(50)' | YES | bytearray(b'\xe5\x88\x86\xe7\xb1\xbb') |
| 17 | CSP | b'decimal(18,4)' | YES | bytearray(b'\xe8\xb5\x84\xe6\x9c\xac\xe6\x94\xaf\xe5\x87\xba\xe5\xa2\x9e\xe9\x80\x9f') |
| 16 | CSP_TTM | b'decimal(18,4)' | YES | bytearray(b'\xe8\xb5\x84\xe6\x9c\xac\xe6\x94\xaf\xe5\x87\xba\xe5\xa2\x9e\xe9\x80\x9fTTM') |
| 3 | Cylce | b'varchar(10)' | YES | bytearray(b'\xe5\x91\xa8\xe6\x9c\x9f') |
| 2 | DataTime | b'datetime' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\x97\xb6\xe9\x97\xb4\xe8\x8a\x82\xe7\x82\xb9') |
| 6 | Debt_Then_Asset | b'decimal(18,4)' | YES | bytearray(b'Debt\xe6\xaf\x94Asset') |
| 9 | DNNPGR_TTM | b'decimal(18,4)' | YES | bytearray(b'\xe6\x89\xa3\xe9\x9d\x9e\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6\xe5\xa2\x9e\xe9\x80\x9fTTM') |
| 11 | GPM | b'decimal(18,4)' | YES | bytearray(b'\xe6\xaf\x9b\xe5\x88\xa9\xe7\x8e\x87') |
| 12 | GPM_TTM | b'decimal(18,4)' | YES | bytearray(b'\xe6\xaf\x9b\xe5\x88\xa9\xe7\x8e\x87TTM') |
| 1 | ID | b'int(11)' | NO | bytearray(b'\xe8\x87\xaa\xe5\xa2\x9e') |
| 10 | Inv_growth | b'decimal(18,4)' | YES | bytearray(b'\xe5\xba\x93\xe5\xad\x98\xe5\xa2\x9e\xe9\x80\x9f') |
| 21 | JSID | b'bigint(20)' | YES | bytearray(b'JSID') |
| 19 | Liab_Then_Asset | b'decimal(18,4)' | YES | bytearray(b'\xe6\x80\xbb\xe8\xb4\x9f\xe5\x80\xba\xe6\xaf\x94Asset') |
| 8 | OCF_Then_Inc_TTM | b'decimal(18,4)' | YES | bytearray(b'\xe7\xbb\x8f\xe8\x90\xa5\xe6\x80\xa7\xe7\x8e\xb0\xe9\x87\x91\xe6\xb5\x81\xe6\xaf\x94\xe6\x94\xb6\xe5\x85\xa5TTM') |
| 15 | OIG | b'decimal(18,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5\xe5\xa2\x9e\xe9\x80\x9f') |
| 14 | OIG_TTM | b'decimal(18,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5\xe5\xa2\x9e\xe9\x80\x9fTTM') |
| 7 | PNPGR_TTM | b'decimal(18,4)' | YES | bytearray(b'\xe5\xbd\x92\xe6\xaf\x8d\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6\xe5\xa2\x9e\xe9\x80\x9fTTM') |
| 20 | UpdateTime | b'datetime' | YES | bytearray(b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4') |



### s02_mfile_yanbao_file () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | File_Id | b'varchar(100)' | NO | bytearray(b'') |
| 3 | File_Name | b'varchar(200)' | NO | bytearray(b'') |
| 13 | File_Path | b'varchar(100)' | NO | bytearray(b'') |
| 7 | File_Type | b'varchar(10)' | NO | bytearray(b'') |
| 14 | From_Mail | b'varchar(50)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 9 | Level_Power | b'int(11)' | NO | bytearray(b'') |
| 11 | Make_Datetime | b'datetime(6)' | NO | bytearray(b'') |
| 6 | Recv_Grandson_Source | b'varchar(30)' | NO | bytearray(b'') |
| 5 | Recv_Son_Source | b'varchar(30)' | NO | bytearray(b'') |
| 4 | Recv_Source | b'varchar(30)' | NO | bytearray(b'') |
| 10 | Tag | b'varchar(10)' | NO | bytearray(b'') |
| 8 | Title | b'varchar(200)' | NO | bytearray(b'') |
| 12 | UpDatetime | b'datetime(6)' | NO | bytearray(b'') |



### s02_onorder () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | direction | b'varchar(20)' | NO | bytearray(b'') |
| 16 | exchangeid | b'varchar(10)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 14 | inserttime | b'varchar(20)' | NO | bytearray(b'') |
| 5 | instrumentid | b'varchar(20)' | NO | bytearray(b'') |
| 2 | investorid | b'varchar(20)' | NO | bytearray(b'') |
| 8 | limitprice | b'decimal(30,15)' | NO | bytearray(b'') |
| 15 | localdate | b'datetime(6)' | NO | bytearray(b'') |
| 7 | offsetflag | b'varchar(20)' | NO | bytearray(b'') |
| 10 | orderstatus | b'varchar(1)' | NO | bytearray(b'') |
| 4 | ordersysid | b'varchar(30)' | NO | bytearray(b'') |
| 3 | userid | b'varchar(20)' | NO | bytearray(b'') |
| 17 | userorderlocalid | b'varchar(20)' | NO | bytearray(b'') |
| 9 | volume | b'int(11)' | NO | bytearray(b'') |
| 13 | volumecancled | b'int(11)' | NO | bytearray(b'') |
| 12 | volumeremain | b'int(11)' | NO | bytearray(b'') |
| 11 | volumetraded | b'int(11)' | NO | bytearray(b'') |



### s02_proxyip () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | Available | b'int(11)' | YES | bytearray(b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\xaf\xe7\x94\xa8') |
| 1 | IP | b'varchar(15)' | NO | bytearray(b'IP\xe5\x9c\xb0\xe5\x9d\x80') |
| 4 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 2 | Port | b'varchar(15)' | YES | bytearray(b'\xe7\xab\xaf\xe5\x8f\xa3\xe5\x8f\xb7') |
| 3 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 6 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_proxypool () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | Available | b'int(2)' | YES | bytearray(b'') |
| 8 | City | b'varchar(30)' | YES | bytearray(b'') |
| 5 | Country | b'varchar(20)' | YES | bytearray(b'') |
| 6 | Country_ID | b'varchar(20)' | YES | bytearray(b'') |
| 1 | IP | b'varchar(20)' | NO | bytearray(b'') |
| 9 | ISP | b'varchar(50)' | YES | bytearray(b'') |
| 11 | Organization | b'varchar(100)' | YES | bytearray(b'') |
| 2 | Port | b'varchar(20)' | NO | bytearray(b'') |
| 7 | Region | b'varchar(30)' | YES | bytearray(b'') |
| 10 | Source | b'varchar(200)' | YES | bytearray(b'') |
| 12 | Updatetime | b'datetime' | YES | bytearray(b'') |
| 4 | UseDatetime | b'datetime' | YES | bytearray(b'') |



### s02_real_time_quotes () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 2 | InstrumentID | b'varchar(15)' | NO | bytearray(b'') |



### s02_s002_cn_stock (中国股指数据表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | CN_Company_Name | b'varchar(50)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d') |
| 2 | Cylce | b'varchar(10)' | YES | bytearray(b'\xe5\x91\xa8\xe6\x9c\x9f') |
| 1 | DataTime | b'datetime' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\x97\xb6\xe9\x97\xb4\xe8\x8a\x82\xe7\x82\xb9') |
| 12 | deductedprofit_ttm2 | b'decimal(18,4)' | YES | bytearray(b'\xe6\x89\xa3\xe9\x99\xa4\xe9\x9d\x9e\xe7\xbb\x8f\xe5\xb8\xb8\xe6\x80\xa7\xe6\x8d\x9f\xe7\x9b\x8a\xe5\x90\x8e\xe7\x9a\x84\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6\xef\xbc\x88\xe9\x9d\x9eTTM\xef\xbc\x89') |
| 7 | eqy_belongto_parcomsh | b'decimal(18,4)' | YES | bytearray(b'\xe5\xbd\x92\xe5\xb1\x9e\xe6\xaf\x8d\xe5\x85\xac\xe5\x8f\xb8\xe8\x82\xa1\xe4\xb8\x9c\xe7\x9a\x84\xe6\x9d\x83\xe7\x9b\x8a') |
| 15 | grossmargin_ttm2 | b'decimal(18,4)' | YES | bytearray(b'\xe6\xaf\x9b\xe5\x88\xa9 TTM') |
| 6 | interestdebt | b'decimal(18,4)' | YES | bytearray(b'\xe5\xb8\xa6\xe6\x81\xaf\xe5\x80\xba\xe5\x8a\xa1') |
| 13 | inventories | b'decimal(18,4)' | YES | bytearray(b'\xe5\xba\x93\xe5\xad\x98') |
| 20 | JSID | b'bigint(20)' | YES | bytearray(b'JSID') |
| 16 | monetary_cap | b'decimal(18,4)' | YES | bytearray(b'\xe8\xb4\xa7\xe5\xb8\x81\xe8\xb5\x84\xe9\x87\x91') |
| 8 | netprofit_ttm2 | b'decimal(18,4)' | YES | bytearray(b'\xe5\xbd\x92\xe5\xb1\x9e\xe6\xaf\x8d\xe5\x85\xac\xe5\x8f\xb8\xe8\x82\xa1\xe4\xb8\x9c\xe7\x9a\x84\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6') |
| 17 | notes_rcv | b'decimal(18,4)' | YES | bytearray(b'\xe5\xba\x94\xe6\x94\xb6\xe7\xa5\xa8\xe6\x8d\xae') |
| 10 | operatecashflow_ttm2 | b'decimal(18,4)' | YES | bytearray(b'\xe7\xbb\x8f\xe8\x90\xa5\xe6\xb4\xbb\xe5\x8a\xa8\xe7\x8e\xb0\xe9\x87\x91\xe5\x87\x80\xe6\xb5\x81\xe9\x87\x8f(TTM)') |
| 9 | or_ttm2 | b'decimal(18,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5\xef\xbc\x88TTM\xef\xbc\x89') |
| 18 | qfa_cash_pay_acq_const_fiolta | b'decimal(18,4)' | YES | bytearray(b'\xe5\x8d\x95\xe5\xad\xa3\xe5\xba\xa6.\xe8\xb4\xad\xe5\xbb\xba\xe5\x9b\xba\xe5\xae\x9a\xe8\xb5\x84\xe4\xba\xa7\xe3\x80\x81\xe6\x97\xa0\xe5\xbd\xa2\xe8\xb5\x84\xe4\xba\xa7\xe5\x92\x8c\xe5\x85\xb6\xe4\xbb\x96\xe9\x95\xbf\xe6\x9c\x9f\xe8\xb5\x84\xe4\xba\xa7\xe6\x94\xaf\xe4\xbb\x98\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 14 | qfa_grossmargin | b'decimal(18,4)' | YES | bytearray(b'\xe5\x8d\x95\xe5\xad\xa3\xe5\xba\xa6.\xe6\xaf\x9b\xe5\x88\xa9') |
| 11 | qfa_oper_rev | b'decimal(18,4)' | YES | bytearray(b'\xe5\x8d\x95\xe5\xad\xa3\xe5\xba\xa6.\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5') |
| 5 | tot_assets | b'decimal(18,4)' | YES | bytearray(b'\xe6\x80\xbb\xe8\xb5\x84\xe4\xba\xa7') |
| 4 | tot_liab | b'decimal(18,4)' | YES | bytearray(b'\xe6\x80\xbb\xe8\xb4\x9f\xe5\x80\xba') |
| 19 | UpdateTime | b'datetime' | YES | bytearray(b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4') |



### s02_tb_emp () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | contract_info | b'text' | NO | bytearray(b'') |
| 2 | contract_name | b'varchar(20)' | NO | bytearray(b'') |
| 4 | contract_using | b'tinyint(1)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |



### s02_tb_investorid () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 2 | investorid | b'varchar(20)' | NO | bytearray(b'') |



### s02_trading () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | direction_stop | b'longtext' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 2 | investorid | b'varchar(20)' | NO | bytearray(b'') |
| 6 | pricetick | b'decimal(18,8)' | NO | bytearray(b'') |
| 3 | ticker | b'varchar(10)' | NO | bytearray(b'') |
| 5 | volumes | b'int(11)' | NO | bytearray(b'') |



### s02_us_bos_difx () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 11 | AWC | b'decimal(18,13)' | YES | bytearray(b'') |
| 21 | AWF | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | CEF | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 6 | DTC | b'decimal(18,8)' | YES | bytearray(b'') |
| 16 | DTF | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | GAC | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | GAF | b'decimal(18,14)' | YES | bytearray(b'') |
| 7 | IVC | b'decimal(18,9)' | YES | bytearray(b'') |
| 17 | IVF | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 10 | NEC | b'decimal(18,12)' | YES | bytearray(b'') |
| 20 | NEF | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | NOC | b'decimal(18,5)' | YES | bytearray(b'') |
| 13 | NOF | b'decimal(18,15)' | YES | bytearray(b'') |
| 27 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 25 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | PPC | b'decimal(18,10)' | YES | bytearray(b'') |
| 18 | PPF | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | PRC | b'decimal(18,11)' | YES | bytearray(b'') |
| 19 | PRF | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | SHC | b'decimal(18,6)' | YES | bytearray(b'') |
| 14 | SHF | b'decimal(18,16)' | YES | bytearray(b'') |
| 26 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 23 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 5 | UOC | b'decimal(18,7)' | YES | bytearray(b'') |
| 15 | UOF | b'decimal(18,17)' | YES | bytearray(b'') |
| 28 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_building_expenditure_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 51 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 54 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 52 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 30 | Private_Amusement_and_recreation | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Private_Commercial | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Private_Communication | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Private_Educational | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Private_Health_care | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Private_Lodging | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Private_Manufacturing | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Private_Nonresidential | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Private_Office | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Private_Power | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Private_Religious | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Private_Residential | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Private_Transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Public_Amusement_and_recreation | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Public_Commercial | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | Public_Educational | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Public_Health_care | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Public_Highway_and_street | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Public_Nonresidential | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Public_Office | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Public_Power | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Public_Public_safety | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Public_Residential | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Public_Transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | PublicConservation_and_development | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | PublicSewage_and_waste_disposal | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | PublicWater_supply | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 50 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 12 | Total_Amusement_and_recreation | b'decimal(18,4)' | NO | bytearray(b'') |
| 7 | Total_Commercial | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Total_Communication | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Total_Conservation_and_development | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Total_Construction | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Total_Educational | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Total_Health_care | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Total_Highway_and_street | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Total_Lodging | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Total_Manufacturing | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Total_Nonresidential | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Total_Office | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Total_Power | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Total_Private_Construction | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Total_Public_Construction | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Total_Public_safety | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Total_Religious | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Total_Residential | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Total_Sewage_and_waste_disposal | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Total_Transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Total_Water_supply | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_commercial_bank_assets_and_liabilities_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 38 | B_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tBorrowings, all commercial banks, seasonally adjusted\t') |
| 2 | B_c_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tBank credit, all commercial banks, seasonally adjusted\t') |
| 30 | C_a_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tCash assets, all commercial banks, seasonally adjusted\t') |
| 11 | C_a_i_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tCommercial and industrial loans, all commercial banks, seasonally adjusted\t') |
| 21 | C_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tConsumer loans, all commercial banks, seasonally adjusted\t') |
| 22 | C_l_C_c_a_o_r_p_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tConsumer loans: Credit cards and other revolving plans, all commercial banks, seasonally adjusted\t') |
| 23 | C_l_O_c_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tConsumer loans: Other consumer loans, all commercial banks, seasonally adjusted\t') |
| 24 | C_l_O_c_l_A_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tConsumer loans: Other consumer loans: Automobile loans, all commercial banks, seasonally adjusted\t') |
| 25 | C_l_O_c_l_A_o_c_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tConsumer loans: Other consumer loans: All other consumer loans, all commercial banks, seasonally adjusted\t') |
| 35 | D_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tDeposits, all commercial banks, seasonally adjusted\t') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 31 | F_f_s_a_s_p_u_a_t_r | b'decimal(18,4)' | YES | bytearray(b'\tFederal funds sold and securities purchased under agreement to resell\t') |
| 29 | L_A_f_l_a_l_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tLESS: Allowance for loan and lease losses, all commercial banks, seasonally adjusted\t') |
| 10 | L_a_l_i_b_c_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tLoans and leases in bank credit, all commercial banks, seasonally adjusted\t') |
| 32 | L_t_c_b_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tLoans to commercial banks, all commercial banks, seasonally adjusted\t') |
| 36 | L_t_d_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tLarge time deposits, all commercial banks, seasonally adjusted\t') |
| 46 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 39 | N_d_t_r_f_o_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tNet due to related foreign offices, all commercial banks, seasonally adjusted\t') |
| 43 | N_u_g_l_o_a_f_s_s_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tNet unrealized gains (losses) on available-for-sale securities, all commercial banks, seasonally adjusted\t') |
| 33 | O_a_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tOther assets, all commercial banks, seasonally adjusted\t') |
| 37 | O_d_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tOther deposits, all commercial banks, seasonally adjusted\t') |
| 40 | O_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tOther liabilities, all commercial banks, seasonally adjusted\t') |
| 26 | O_l_a_l_A_o_l_a_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tOther loans and leases: All other loans and leases, all commercial banks, seasonally adjusted\t') |
| 27 | O_l_a_l_A_o_l_a_l_L_t_n_f_i_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tOther loans and leases: All other loans and leases: Loans to nondepository financial institutions, all commercial banks, seasonally adjusted\t') |
| 28 | O_l_a_l_A_o_l_a_l_O_l_n_e_c_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tOther loans and leases: All other loans and leases: Other loans not elsewhere classified, all commercial banks, seasonally adjusted\t') |
| 7 | O_s_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tOther securities, all commercial banks, seasonally adjusted\t') |
| 8 | O_s_M_b_s_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tOther securities: Mortgage-backed securities, all commercial banks, seasonally adjusted\t') |
| 9 | O_s_N_M_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tOther securities: Non-MBS, all commercial banks, seasonally adjusted\t') |
| 49 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 47 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 42 | R_a_l_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tResidual (assets less liabilities), all commercial banks, seasonally adjusted\t') |
| 12 | R_e_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tReal estate loans, all commercial banks, seasonally adjusted\t') |
| 16 | R_e_l_C_r_e_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tReal estate loans: Commercial real estate loans, all commercial banks, seasonally adjusted\t') |
| 17 | R_e_l_C_r_e_l_C_a_l_d_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tReal estate loans: Commercial real estate loans: Construction and land development loans, all commercial banks, seasonally adjusted\t') |
| 18 | R_e_l_C_r_e_l_S_b_f_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tReal estate loans: Commercial real estate loans: Secured by farmland, all commercial banks, seasonally adjusted\t') |
| 19 | R_e_l_C_r_e_l_S_b_m_p_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tReal estate loans: Commercial real estate loans: Secured by multifamily properties, all commercial banks, seasonally adjusted\t') |
| 20 | R_e_l_C_r_e_l_S_b_n_n_p_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tReal estate loans: Commercial real estate loans: Secured by nonfarm nonresidential properties, all commercial banks, seasonally adjusted\t') |
| 13 | R_e_l_R_r_e_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tReal estate loans: Residential real estate loans, all commercial banks, seasonally adjusted\t') |
| 15 | R_e_l_R_r_e_l_C_e_r_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tReal estate loans: Residential real estate loans: Closed-end residential loans, all commercial banks, seasonally adjusted\t') |
| 14 | R_e_l_R_r_e_l_R_h_e_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tReal estate loans: Residential real estate loans: Revolving home equity loans, all commercial banks, seasonally adjusted\t') |
| 3 | S_i_b_c_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tSecurities in bank credit, all commercial banks, seasonally adjusted\t') |
| 48 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 45 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 34 | T_a_a_o_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tTotal assets, all commercial banks, seasonally adjusted\t') |
| 4 | T_a_a_s_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tTreasury and agency securities, all commercial banks, seasonally adjusted\t') |
| 5 | T_a_a_s_M_b_s_M_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tTreasury and agency securities: Mortgage-backed securities (MBS), all commercial banks, seasonally adjusted\t') |
| 6 | T_a_a_s_N_M_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tTreasury and agency securities: Non-MBS, all commercial banks, seasonally adjusted\t') |
| 41 | T_l_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tTotal liabilities, all commercial banks, seasonally adjusted\t') |
| 44 | U_S_T_a_a_s_M_a_c_b_s_a | b'decimal(18,4)' | YES | bytearray(b'\tU.S. Treasury and agency securities, MBS, all commercial banks, seasonally adjusted\t') |
| 50 | Updatetime | b'datetime' | YES | bytearray(b'') |



### s02_us_corporate_profits_by_industry_a () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 27 | Chemical_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Computer_and_electronic_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Corporate_profits_with_inventory_valuation_adjustment | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | CorporateProfits_InventVal_CapitalConAdj | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 3 | Domestic_industries_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Domestic_industries_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Electrical_equipment_appliances_and_components | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Fabricated_metal_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Federal_Reserve_banks | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Financial | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Financial1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Food_and_beverage_and_tobacco_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Information | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Less_Payments_to_the_rest_of_the_world | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Machinery | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Manufacturing | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 22 | Motor_vehicles_bodies_and_trailers_and_parts | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Nonfinancial_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Nonfinancial_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 23 | Other_durable_goods3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Other_financial2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Other_nondurable_goods4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Other_nonfinancial5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 26 | Petroleum_and_coal_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Receipts_from_the_rest_of_the_world | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Rest_of_the_world_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Rest_of_the_world_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Retail_trade | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 35 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 31 | Transportation_and_warehousing | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Updatetime | b'datetime' | YES | bytearray(b'') |
| 15 | Utilities | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Wholesale_trade | b'decimal(18,4)' | YES | bytearray(b'') |



### s02_us_corporate_profits_by_industry_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 27 | Chemical_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Computer_and_electronic_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Corporate_profits_with_inventory_valuation_adjustment | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | CorporateProfits_InventVal_CapitalConAdj | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 3 | Domestic_industries_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Domestic_industries_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Electrical_equipment_appliances_and_components | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Fabricated_metal_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Federal_Reserve_banks | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Financial | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Financial1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Food_and_beverage_and_tobacco_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Information | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Less_Payments_to_the_rest_of_the_world | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Machinery | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Manufacturing | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 22 | Motor_vehicles_bodies_and_trailers_and_parts | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Nonfinancial_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Nonfinancial_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 23 | Other_durable_goods3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Other_financial2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Other_nondurable_goods4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Other_nonfinancial5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 26 | Petroleum_and_coal_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Receipts_from_the_rest_of_the_world | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Rest_of_the_world_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Rest_of_the_world_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Retail_trade | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 35 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 31 | Transportation_and_warehousing | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Updatetime | b'datetime' | YES | bytearray(b'') |
| 15 | Utilities | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Wholesale_trade | b'decimal(18,4)' | YES | bytearray(b'') |



### s02_us_domestic_buyer_final_sales_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 8 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 7 | Equals_Final_sales_to_domestic_purchasers | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Equals_Gross_domestic_purchases | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Final_sales_of_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Final_sales_to_private_domestic_purchasers1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Less_Change_in_private_inventories | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Less_Exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 15 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 13 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 4 | Plus_Imports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 11 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 16 | Updatetime | b'datetime' | YES | bytearray(b'') |



### s02_us_employment_cost_index_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 2 | Employment_cost_index | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'') |



### s02_us_esms_seasonallyadjusted_diffusion () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 11 | AWCDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | AWFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | CEFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 6 | DTCDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | DTFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | GACDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | GAFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | IVCDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | IVFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 10 | NECDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | NEFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | NOCDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | NOFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 26 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | PPCDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | PPFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | PRCDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | PRFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | SHCDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | SHFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 24 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 23 | TSFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | UOCDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | UOFDISA | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_export_price () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | All_exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Automotive_vehicles_parts_and_engines | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Capital_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Consumer_goods_excluding_automotives | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 3 | Foods_feeds_and_beverages | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Industrial_supplies_and_materials | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 12 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 10 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 11 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 8 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 13 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_foreign_trade_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 35 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Balance_on_current_account_NIPAs_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Balance_on_current_account_NIPAs_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | C_t_c_f_g_s_i_a_t_r_f_t_r_o_t_w | b'decimal(18,4)' | YES | bytearray(b'Current_taxes_contributions_for_government_social_insurance_and_transfer_receipts_from_the_rest_of_the_world2') |
| 18 | Current_payments_to_the_rest_of_the_world | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Current_receipts_from_the_rest_of_the_world | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Current_taxes_and_transfer_payments_to_the_rest_of_the_world2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 12 | Dividends_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Dividends_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Durable_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Durable_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | From_business | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | From_government | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | From_persons | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Imports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Income_payments | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Income_payments_on_assets | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Income_receipts | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Income_receipts_on_assets | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Interest_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Interest_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Less_Capital_account_transactions_net_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 36 | Net_lending_or_net_borrowing_NIPAs | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Nondurable_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Nondurable_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 41 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 29 | R_e_o_f_d_i_i_t_U_S | b'decimal(18,4)' | YES | bytearray(b'Reinvested_earnings_on_foreign_direct_investment_in_the_United_States') |
| 13 | Reinvested_earnings_on_U_S_direct_investment_abroad | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Services_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Services_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 39 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 16 | To_business | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | To_government | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | To_persons | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 25 | Wage_and_salary_payments | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Wage_and_salary_receipts | b'decimal(18,4)' | YES | bytearray(b'') |



### s02_us_foreign_trade_q_copy1 () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 35 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Balance_on_current_account_NIPAs_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Balance_on_current_account_NIPAs_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | C_t_c_f_g_s_i_a_t_r_f_t_r_o_t_w | b'decimal(18,4)' | YES | bytearray(b'Current_taxes_contributions_for_government_social_insurance_and_transfer_receipts_from_the_rest_of_the_world2') |
| 18 | Current_payments_to_the_rest_of_the_world | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Current_receipts_from_the_rest_of_the_world | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Current_taxes_and_transfer_payments_to_the_rest_of_the_world2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 12 | Dividends_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Dividends_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Durable_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Durable_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | From_business | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | From_government | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | From_persons | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Imports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Income_payments | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Income_payments_on_assets | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Income_receipts | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Income_receipts_on_assets | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Interest_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Interest_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Less_Capital_account_transactions_net_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 36 | Net_lending_or_net_borrowing_NIPAs | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Nondurable_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Nondurable_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 41 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 29 | R_e_o_f_d_i_i_t_U_S | b'decimal(18,4)' | YES | bytearray(b'Reinvested_earnings_on_foreign_direct_investment_in_the_United_States') |
| 13 | Reinvested_earnings_on_U_S_direct_investment_abroad | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Services_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Services_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 39 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 16 | To_business | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | To_government | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | To_persons | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 25 | Wage_and_salary_payments | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Wage_and_salary_receipts | b'decimal(18,4)' | YES | bytearray(b'') |



### s02_us_foreign_trade_y () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 35 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Balance_on_current_account_NIPAs_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Balance_on_current_account_NIPAs_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | C_t_c_f_g_s_i_a_t_r_f_t_r_o_t_w | b'decimal(18,4)' | YES | bytearray(b'Current_taxes_contributions_for_government_social_insurance_and_transfer_receipts_from_the_rest_of_the_world2') |
| 18 | Current_payments_to_the_rest_of_the_world | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Current_receipts_from_the_rest_of_the_world | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Current_taxes_and_transfer_payments_to_the_rest_of_the_world2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 12 | Dividends_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Dividends_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Durable_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Durable_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | From_business | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | From_government | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | From_persons | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Imports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Income_payments | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Income_payments_on_assets | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Income_receipts | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Income_receipts_on_assets | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Interest_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Interest_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Less_Capital_account_transactions_net_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 36 | Net_lending_or_net_borrowing_NIPAs | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Nondurable_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Nondurable_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 41 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 29 | R_e_o_f_d_i_i_t_U_S | b'decimal(18,4)' | YES | bytearray(b'Reinvested_earnings_on_foreign_direct_investment_in_the_United_States') |
| 13 | Reinvested_earnings_on_U_S_direct_investment_abroad | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Services_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Services_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 39 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 16 | To_business | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | To_government | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | To_persons | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 25 | Wage_and_salary_payments | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Wage_and_salary_receipts | b'decimal(18,4)' | YES | bytearray(b'') |



### s02_us_frb_g17_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | Value | b'decimal(18,4)' | YES | bytearray(b'') |



### s02_us_frb_g17_y () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | Value | b'decimal(18,4)' | YES | bytearray(b'') |



### s02_us_frb_h8 () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | B1001NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | B1002NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | B1003NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | B1011NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | B1020NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | B1023NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | B1026NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | B1027NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | B1029NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | B1030NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | B1043NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | B1047NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | B1048NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | B1058NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | B1072NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | B1091NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | B1100NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | B1110NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | B1151NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | B1152NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | B1215NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | B1216NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | B1217NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | B1218NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | B1220NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | B1221NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | B1231NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | B1243NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | B1245NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | B1247NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | B1301NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | B1302NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | B1303NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | B1304NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | B1310NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | B3053NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | B3092NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | B3094NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | B3095NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | B3219NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | B3248NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | B3305NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | B8321NCBAM | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 46 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 49 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 47 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 48 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 45 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 50 | Updatetime | b'datetime' | YES | bytearray(b'') |



### s02_us_gdp_a () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 15 | Change_in_private_inventories | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 5 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Federal | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Fixed_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Government_consumption_expenditures_and_gross_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Gross_private_domestic_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Intellectual_property_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 25 | National_defense | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Net_exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Nondefense | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Nonresidential | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 30 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 3 | Personal_consumption_expenditures | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Residential | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Services | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Services_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Services_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 28 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 27 | State_and_local | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Structures | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_gdp_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 15 | Change_in_private_inventories | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 5 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Federal | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Fixed_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Government_consumption_expenditures_and_gross_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Gross_private_domestic_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Intellectual_property_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 25 | National_defense | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Net_exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Nondefense | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Nonresidential | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 30 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 3 | Personal_consumption_expenditures | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Residential | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Services | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Services_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Services_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 28 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 27 | State_and_local | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Structures | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_import_and_export_by_product_category_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 50 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Automotive_vehicles_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Automotive_vehicles_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Capital_goods_except_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Capital_goods_except_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Charges_for_the_use_of_intellectual_property_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Charges_for_the_use_of_intellectual_property_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Civilian_aircraft_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Civilian_aircraft_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Computers_peripherals_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Computers_peripherals_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Consumer_goods_except_food_and_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Consumer_goods_except_food_and_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 6 | Durable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Durable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Durable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Durable_goods_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Exports_of_agricultural_goods4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 51 | Exports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Exports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 54 | Exports_of_nonagricultural_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 52 | Exports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Exports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Foods_feeds_and_beverages_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Foods_feeds_and_beverages_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Government_goods_and_services_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Government_goods_and_services_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | Imports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Imports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Imports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 56 | Imports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 57 | Imports_of_nonpetroleum_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Imports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Industrial_supplies_and_materials_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Industrial_supplies_and_materials_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 59 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Nondurable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Nondurable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Nondurable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | Nondurable_goods_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Nondurable_goods_excluding_petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Nondurable_goods_excluding_petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 62 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 18 | Other2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Other_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Other_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Other_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Other_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Other_5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Other_business_services3_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Other_business_services3_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 60 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | Petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 61 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 58 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 20 | Transport_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Transport_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Travel_for_all_purposes_including_education_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Travel_for_all_purposes_including_education_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 63 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_import_and_export_by_product_category_y () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 50 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Automotive_vehicles_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Automotive_vehicles_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Capital_goods_except_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Capital_goods_except_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Charges_for_the_use_of_intellectual_property_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Charges_for_the_use_of_intellectual_property_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Civilian_aircraft_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Civilian_aircraft_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Computers_peripherals_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Computers_peripherals_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Consumer_goods_except_food_and_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Consumer_goods_except_food_and_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 6 | Durable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Durable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Durable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Durable_goods_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Exports_of_agricultural_goods4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 51 | Exports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Exports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 54 | Exports_of_nonagricultural_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 52 | Exports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Exports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Foods_feeds_and_beverages_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Foods_feeds_and_beverages_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Government_goods_and_services_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Government_goods_and_services_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | Imports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Imports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Imports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 56 | Imports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 57 | Imports_of_nonpetroleum_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Imports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Industrial_supplies_and_materials_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Industrial_supplies_and_materials_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 59 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Nondurable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Nondurable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Nondurable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | Nondurable_goods_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Nondurable_goods_excluding_petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Nondurable_goods_excluding_petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 62 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 18 | Other2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Other_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Other_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Other_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Other_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Other_5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Other_business_services3_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Other_business_services3_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 60 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | Petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 61 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 58 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 20 | Transport_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Transport_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Travel_for_all_purposes_including_education_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Travel_for_all_purposes_including_education_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 63 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_import_and_export_price_index_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 50 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Automotive_vehicles_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Automotive_vehicles_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Capital_goods_except_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Capital_goods_except_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Charges_for_the_use_of_intellectual_property_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Charges_for_the_use_of_intellectual_property_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Civilian_aircraft_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Civilian_aircraft_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Computers_peripherals_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Computers_peripherals_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Consumer_goods_except_food_and_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Consumer_goods_except_food_and_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 6 | Durable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Durable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Durable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Durable_goods_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Exports_of_agricultural_goods4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 51 | Exports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Exports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 54 | Exports_of_nonagricultural_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 52 | Exports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Exports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Foods_feeds_and_beverages_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Foods_feeds_and_beverages_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Government_goods_and_services_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Government_goods_and_services_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | Imports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Imports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Imports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 56 | Imports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 57 | Imports_of_nonpetroleum_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Imports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Industrial_supplies_and_materials_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Industrial_supplies_and_materials_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 59 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Nondurable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Nondurable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Nondurable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | Nondurable_goods_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Nondurable_goods_excluding_petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Nondurable_goods_excluding_petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 62 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 18 | Other2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Other_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Other_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Other_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Other_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Other_5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Other_business_services3_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Other_business_services3_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 60 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | Petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 61 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 58 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 20 | Transport_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Transport_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Travel_for_all_purposes_including_education_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Travel_for_all_purposes_including_education_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 63 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_import_and_export_price_index_y () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 50 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Automotive_vehicles_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Automotive_vehicles_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Capital_goods_except_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Capital_goods_except_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Charges_for_the_use_of_intellectual_property_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Charges_for_the_use_of_intellectual_property_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Civilian_aircraft_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Civilian_aircraft_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Computers_peripherals_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Computers_peripherals_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Consumer_goods_except_food_and_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Consumer_goods_except_food_and_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 6 | Durable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Durable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Durable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Durable_goods_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Exports_of_agricultural_goods4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 51 | Exports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Exports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 54 | Exports_of_nonagricultural_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 52 | Exports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Exports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Foods_feeds_and_beverages_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Foods_feeds_and_beverages_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Government_goods_and_services_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Government_goods_and_services_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | Imports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Imports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Imports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 56 | Imports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 57 | Imports_of_nonpetroleum_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Imports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Industrial_supplies_and_materials_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Industrial_supplies_and_materials_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 59 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Nondurable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Nondurable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Nondurable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | Nondurable_goods_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Nondurable_goods_excluding_petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Nondurable_goods_excluding_petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 62 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 18 | Other2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Other_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Other_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Other_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Other_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Other_5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Other_business_services3_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Other_business_services3_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 60 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | Petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 61 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 58 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 20 | Transport_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Transport_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Travel_for_all_purposes_including_education_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Travel_for_all_purposes_including_education_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 63 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_import_and_export_quantity_index_a () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 50 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Automotive_vehicles_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Automotive_vehicles_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Capital_goods_except_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Capital_goods_except_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Charges_for_the_use_of_intellectual_property_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Charges_for_the_use_of_intellectual_property_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Civilian_aircraft_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Civilian_aircraft_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Computers_peripherals_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Computers_peripherals_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Consumer_goods_except_food_and_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Consumer_goods_except_food_and_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 40 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Durable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Durable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Durable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Exports_of_agricultural_goods4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 51 | Exports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Exports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 54 | Exports_of_nonagricultural_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 52 | Exports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Exports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Foods_feeds_and_beverages_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Foods_feeds_and_beverages_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Government_goods_and_services_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Government_goods_and_services_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | Imports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Imports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Imports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 56 | Imports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 57 | Imports_of_nonpetroleum_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Imports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Industrial_supplies_and_materials_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Industrial_supplies_and_materials_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 59 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 41 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Nondurable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Nondurable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Nondurable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Nondurable_goods_excluding_petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Nondurable_goods_excluding_petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 62 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 18 | Other2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Other_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Other_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Other_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Other_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Other_5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Other_business_services3_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Other_business_services3_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 60 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | Petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 61 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 58 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 20 | Transport_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Transport_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Travel_for_all_purposes_including_education_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Travel_for_all_purposes_including_education_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 63 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_import_and_export_quantity_index_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 50 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Automotive_vehicles_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Automotive_vehicles_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Capital_goods_except_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Capital_goods_except_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Charges_for_the_use_of_intellectual_property_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Charges_for_the_use_of_intellectual_property_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Civilian_aircraft_engines_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Civilian_aircraft_engines_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Computers_peripherals_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Computers_peripherals_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Consumer_goods_except_food_and_automotive_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Consumer_goods_except_food_and_automotive_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 40 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Durable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Durable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Durable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Exports_of_agricultural_goods4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 51 | Exports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Exports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 54 | Exports_of_nonagricultural_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 52 | Exports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Exports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Foods_feeds_and_beverages_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Foods_feeds_and_beverages_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Government_goods_and_services_n_e_c_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Government_goods_and_services_n_e_c_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | Imports_of_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Imports_of_goods1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Imports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 56 | Imports_of_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 57 | Imports_of_nonpetroleum_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Imports_of_services1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Industrial_supplies_and_materials_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Industrial_supplies_and_materials_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 59 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 41 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Nondurable_goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Nondurable_goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Nondurable_goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Nondurable_goods_excluding_petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Nondurable_goods_excluding_petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 62 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 18 | Other2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Other_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Other_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Other_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Other_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Other_5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Other_business_services3_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Other_business_services3_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 60 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | Petroleum_and_products_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Petroleum_and_products_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 61 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 58 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 20 | Transport_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Transport_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Travel_for_all_purposes_including_education_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Travel_for_all_purposes_including_education_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 63 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_import_export_index () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | Agricultural_exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | All_exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | All_imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 3 | Fuel_imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 7 | Nonagricultural_exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Nonfuel_imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 10 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 11 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 8 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 13 | Updatetime | b'datetime' | YES | bytearray(b'') |



### s02_us_import_export_index_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | Agricultural_exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | All_exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | All_imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 3 | Fuel_imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Nonagricultural_exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Nonfuel_imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 10 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 11 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 8 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 13 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_import_price () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | All_imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Automotive_vehicles_parts_and_engines | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Capital_goods | b'varchar(255)' | YES | bytearray(b'') |
| 7 | Consumer_goods_excluding_automotives | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 3 | Foods_feeds_and_beverages | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Industrial_supplies_and_materials | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 12 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 10 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 11 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 8 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 13 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_industrial_value_added_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 87 | Accommodation | b'decimal(18,4)' | YES | bytearray(b'') |
| 86 | Accommodation_and_food_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 99 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 73 | Administrative_and_support_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 72 | Administrative_and_waste_management_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Agriculture_forestry_fishing_and_hunting | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Air_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 78 | Ambulatory_health_care_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 85 | Amusements_gambling_and_recreation_industries | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Apparel_and_leather_and_allied_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 83 | Arts_entertainment_and_recreation | b'decimal(18,4)' | YES | bytearray(b'') |
| 82 | Arts_entertainment_recreation_accommodation_and_food_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Broadcasting_and_telecommunications | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Chemical_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Computer_and_electronic_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 69 | Computer_systems_design_and_related_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Construction | b'decimal(18,4)' | YES | bytearray(b'') |
| 54 | D_p_i_p_a_o_i_s | b'decimal(18,4)' | YES | bytearray(b'Data_processing_internet_publishing_and_other_information_services') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 14 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 76 | Educational_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 75 | Educational_services_health_care_and_social_assistance | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Electrical_equipment_appliances_and_components | b'decimal(18,4)' | YES | bytearray(b'') |
| 57 | F_R_b_c_i_a_r_a | b'decimal(18,4)' | YES | bytearray(b'Federal_Reserve_banks_credit_intermediation_and_related_activities') |
| 18 | Fabricated_metal_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Farms | b'decimal(18,4)' | YES | bytearray(b'') |
| 91 | Federal | b'decimal(18,4)' | YES | bytearray(b'') |
| 56 | Finance_and_insurance | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | Finance_insurance_real_estate_rental_and_leasing | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Food_and_beverage_and_tobacco_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Food_and_beverage_stores | b'decimal(18,4)' | YES | bytearray(b'') |
| 88 | Food_services_and_drinking_places | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Forestry_fishing_and_related_activities | b'decimal(18,4)' | YES | bytearray(b'') |
| 60 | Funds_trusts_and_other_financial_vehicles | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Furniture_and_related_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 92 | General_government_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 97 | General_government_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | General_merchandise_stores | b'decimal(18,4)' | YES | bytearray(b'') |
| 90 | Government | b'decimal(18,4)' | YES | bytearray(b'') |
| 95 | Government_enterprises_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 98 | Government_enterprises_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 77 | Health_care_and_social_assistance | b'decimal(18,4)' | YES | bytearray(b'') |
| 79 | Hospitals | b'decimal(18,4)' | YES | bytearray(b'') |
| 63 | Housing | b'decimal(18,4)' | YES | bytearray(b'') |
| 50 | Information | b'decimal(18,4)' | YES | bytearray(b'') |
| 102 | Information_communications_technology_producing_industries_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 59 | Insurance_carriers_and_related_activities | b'decimal(18,4)' | YES | bytearray(b'') |
| 68 | Legal_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Machinery | b'decimal(18,4)' | YES | bytearray(b'') |
| 71 | Management_of_companies_and_enterprises | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Manufacturing | b'decimal(18,4)' | YES | bytearray(b'') |
| 104 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Mining | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Mining_except_oil_and_gas | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Miscellaneous_manufacturing | b'decimal(18,4)' | YES | bytearray(b'') |
| 70 | Miscellaneous_professional_scientific_and_technical_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 52 | Motion_picture_and_sound_recording_industries | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Motor_vehicle_and_parts_dealers | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Motor_vehicles_bodies_and_trailers_and_parts | b'decimal(18,4)' | YES | bytearray(b'') |
| 93 | National_defense | b'decimal(18,4)' | YES | bytearray(b'') |
| 94 | Nondefense | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Nonmetallic_mineral_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 80 | Nursing_and_residential_care_facilities | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Oil_and_gas_extraction | b'decimal(18,4)' | YES | bytearray(b'') |
| 107 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 64 | Other_real_estate | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Other_retail | b'decimal(18,4)' | YES | bytearray(b'') |
| 89 | Other_services_except_government | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Other_transportation_and_support_activities | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Other_transportation_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Paper_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 84 | Performing_arts_spectator_sports_museums_and_related_activities | b'decimal(18,4)' | YES | bytearray(b'') |
| 105 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 32 | Petroleum_and_coal_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Pipeline_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Plastics_and_rubber_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Primary_metals | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Printing_and_related_support_activities | b'decimal(18,4)' | YES | bytearray(b'') |
| 100 | Private_goods_producing_industries_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Private_industries | b'decimal(18,4)' | YES | bytearray(b'') |
| 101 | Private_services_producing_industries_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 66 | Professional_and_business_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 67 | Professional_scientific_and_technical_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 51 | Publishing_industries_except_internet_includes_software | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Rail_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 62 | Real_estate | b'decimal(18,4)' | YES | bytearray(b'') |
| 61 | Real_estate_and_rental_and_leasing | b'decimal(18,4)' | YES | bytearray(b'') |
| 65 | Rental_and_leasing_services_and_lessors_of_intangible_assets | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Retail_trade | b'decimal(18,4)' | YES | bytearray(b'') |
| 58 | Securities_commodity_contracts_and_investments | b'decimal(18,4)' | YES | bytearray(b'') |
| 81 | Social_assistance | b'decimal(18,4)' | YES | bytearray(b'') |
| 106 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 103 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 96 | State_and_local | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Support_activities_for_mining | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Textile_mills_and_textile_product_mills | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Transit_and_ground_passenger_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | Transportation_and_warehousing | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Truck_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 108 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 11 | Utilities | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Warehousing_and_storage | b'decimal(18,4)' | YES | bytearray(b'') |
| 74 | Waste_management_and_remediation_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Water_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Wholesale_trade | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Wood_products | b'decimal(18,4)' | YES | bytearray(b'') |



### s02_us_industrial_value_added_y () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 87 | Accommodation | b'decimal(18,4)' | YES | bytearray(b'') |
| 86 | Accommodation_and_food_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 99 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 73 | Administrative_and_support_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 72 | Administrative_and_waste_management_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Agriculture_forestry_fishing_and_hunting | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Air_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 78 | Ambulatory_health_care_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 85 | Amusements_gambling_and_recreation_industries | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Apparel_and_leather_and_allied_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 83 | Arts_entertainment_and_recreation | b'decimal(18,4)' | YES | bytearray(b'') |
| 82 | Arts_entertainment_recreation_accommodation_and_food_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Broadcasting_and_telecommunications | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Chemical_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Computer_and_electronic_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 69 | Computer_systems_design_and_related_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Construction | b'decimal(18,4)' | YES | bytearray(b'') |
| 54 | D_p_i_p_a_o_i_s | b'decimal(18,4)' | YES | bytearray(b'Data_processing_internet_publishing_and_other_information_services') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 14 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 76 | Educational_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 75 | Educational_services_health_care_and_social_assistance | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Electrical_equipment_appliances_and_components | b'decimal(18,4)' | YES | bytearray(b'') |
| 57 | F_R_b_c_i_a_r_a | b'decimal(18,4)' | YES | bytearray(b'Federal_Reserve_banks_credit_intermediation_and_related_activities') |
| 18 | Fabricated_metal_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Farms | b'decimal(18,4)' | YES | bytearray(b'') |
| 91 | Federal | b'decimal(18,4)' | YES | bytearray(b'') |
| 56 | Finance_and_insurance | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | Finance_insurance_real_estate_rental_and_leasing | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Food_and_beverage_and_tobacco_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Food_and_beverage_stores | b'decimal(18,4)' | YES | bytearray(b'') |
| 88 | Food_services_and_drinking_places | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Forestry_fishing_and_related_activities | b'decimal(18,4)' | YES | bytearray(b'') |
| 60 | Funds_trusts_and_other_financial_vehicles | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Furniture_and_related_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 92 | General_government_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 97 | General_government_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | General_merchandise_stores | b'decimal(18,4)' | YES | bytearray(b'') |
| 90 | Government | b'decimal(18,4)' | YES | bytearray(b'') |
| 95 | Government_enterprises_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 98 | Government_enterprises_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 77 | Health_care_and_social_assistance | b'decimal(18,4)' | YES | bytearray(b'') |
| 79 | Hospitals | b'decimal(18,4)' | YES | bytearray(b'') |
| 63 | Housing | b'decimal(18,4)' | YES | bytearray(b'') |
| 50 | Information | b'decimal(18,4)' | YES | bytearray(b'') |
| 102 | Information_communications_technology_producing_industries_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 59 | Insurance_carriers_and_related_activities | b'decimal(18,4)' | YES | bytearray(b'') |
| 68 | Legal_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Machinery | b'decimal(18,4)' | YES | bytearray(b'') |
| 71 | Management_of_companies_and_enterprises | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Manufacturing | b'decimal(18,4)' | YES | bytearray(b'') |
| 104 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Mining | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Mining_except_oil_and_gas | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Miscellaneous_manufacturing | b'decimal(18,4)' | YES | bytearray(b'') |
| 70 | Miscellaneous_professional_scientific_and_technical_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 52 | Motion_picture_and_sound_recording_industries | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Motor_vehicle_and_parts_dealers | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Motor_vehicles_bodies_and_trailers_and_parts | b'decimal(18,4)' | YES | bytearray(b'') |
| 93 | National_defense | b'decimal(18,4)' | YES | bytearray(b'') |
| 94 | Nondefense | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Nonmetallic_mineral_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 80 | Nursing_and_residential_care_facilities | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Oil_and_gas_extraction | b'decimal(18,4)' | YES | bytearray(b'') |
| 107 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 64 | Other_real_estate | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Other_retail | b'decimal(18,4)' | YES | bytearray(b'') |
| 89 | Other_services_except_government | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Other_transportation_and_support_activities | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Other_transportation_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Paper_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 84 | Performing_arts_spectator_sports_museums_and_related_activities | b'decimal(18,4)' | YES | bytearray(b'') |
| 105 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 32 | Petroleum_and_coal_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Pipeline_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | Plastics_and_rubber_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Primary_metals | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Printing_and_related_support_activities | b'decimal(18,4)' | YES | bytearray(b'') |
| 100 | Private_goods_producing_industries_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Private_industries | b'decimal(18,4)' | YES | bytearray(b'') |
| 101 | Private_services_producing_industries_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 66 | Professional_and_business_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 67 | Professional_scientific_and_technical_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 51 | Publishing_industries_except_internet_includes_software | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Rail_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 62 | Real_estate | b'decimal(18,4)' | YES | bytearray(b'') |
| 61 | Real_estate_and_rental_and_leasing | b'decimal(18,4)' | YES | bytearray(b'') |
| 65 | Rental_and_leasing_services_and_lessors_of_intangible_assets | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Retail_trade | b'decimal(18,4)' | YES | bytearray(b'') |
| 58 | Securities_commodity_contracts_and_investments | b'decimal(18,4)' | YES | bytearray(b'') |
| 81 | Social_assistance | b'decimal(18,4)' | YES | bytearray(b'') |
| 106 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 103 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 96 | State_and_local | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Support_activities_for_mining | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Textile_mills_and_textile_product_mills | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Transit_and_ground_passenger_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | Transportation_and_warehousing | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Truck_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 108 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 11 | Utilities | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Warehousing_and_storage | b'decimal(18,4)' | YES | bytearray(b'') |
| 74 | Waste_management_and_remediation_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Water_transportation | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Wholesale_trade | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Wood_products | b'decimal(18,4)' | YES | bytearray(b'') |



### s02_us_inflation () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | All_items | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | All_items_less_food_and_energy | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Apparel | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Commodities_less_food_and_energy_commodities | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 18 | Education_and_communication | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Electricity | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Energy | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Food | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Food_at_home | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Food_away_from_home | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Gasoline_all_types | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 14 | Medical_care_commodities | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Medical_care_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Natural_gas_piped | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | New_vehicles | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 21 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 15 | Services_less_energy_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Shelter | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 19 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 24 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_internationalpositionnet_yq () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | A_e_f_d_s_o_l_7_8_10_a_11 | b'decimal(18,4)' | YES | bytearray(b'Assets_excluding_financial_derivatives_sum_of_lines_7_8_10_and_11') |
| 8 | By_functional_category_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | By_functional_category_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 9 | Direct_investment_at_market_value_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Direct_investment_at_market_value_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | F_d_o_t_r_g_n_f_v | b'decimal(18,4)' | YES | bytearray(b'Financial_derivatives_other_than_reserves_gross_negative_fair_value') |
| 16 | F_d_o_t_r_g_n_f_v_l_17 | b'decimal(18,4)' | YES | bytearray(b'Financial_derivatives_other_than_reserves_gross_negative_fair_value_line_17') |
| 11 | F_d_o_t_r_g_p_f_v | b'decimal(18,4)' | YES | bytearray(b'Financial_derivatives_other_than_reserves_gross_positive_fair_value') |
| 7 | F_d_o_t_r_g_p_f_v_l_9 | b'decimal(18,4)' | YES | bytearray(b'Financial_derivatives_other_than_reserves_gross_positive_fair_value_line_9') |
| 4 | F_d_o_t_r_n_l_6_l_l_14 | b'decimal(18,4)' | YES | bytearray(b'Financial_derivatives_other_than_reserves_net_line_6_less_line_14') |
| 15 | L_e_f_d_s_o_l_15_16_a_18 | b'decimal(18,4)' | YES | bytearray(b'Liabilities_excluding_financial_derivatives_sum_of_lines_15_16_and_18') |
| 23 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 3 | N_i_i_p_e_f_d_l_5_l_l_13 | b'decimal(18,4)' | YES | bytearray(b'Net_international_investment_position_excluding_financial_derivatives_line_5_less_line_13') |
| 26 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 12 | Other_investment_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Other_investment_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 10 | Portfolio_investment_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Portfolio_investment_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Reserve_assets | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 22 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 5 | U_S_assets | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | U_S_liabilities | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | U_S_n_i_i_p_l_4_l_l_12 | b'decimal(18,4)' | YES | bytearray(b'U_S_net_international_investment_position_line_4_less_line_12') |
| 27 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_jolt_job_openings () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 2 | Job_Openings | b'int(8)' | YES | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_m3_durable_goods_inventory_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | value | b'decimal(18,4)' | YES | bytearray(b'') |



### s02_us_m3_durable_goods_new_order_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | value | b'decimal(18,4)' | YES | bytearray(b'') |



### s02_us_m3_durable_goods_shipment_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | value | b'decimal(18,4)' | YES | bytearray(b'') |



### s02_us_m3inventories_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | value | b'decimal(18,4)' | YES | bytearray(b'') |



### s02_us_m3neworders_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | value | b'decimal(18,4)' | YES | bytearray(b'') |



### s02_us_m3value_of_shipment_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | value | b'decimal(18,4)' | YES | bytearray(b'') |



### s02_us_michigan_consumer_sentiment () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 2 | Michigan_University_Consumer_Sentiment | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_nahb_wells_fargo_national_hmi_components_history () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | category | b'varchar(100)' | NO | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 5 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 8 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 6 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 7 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 4 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 9 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 3 | value | b'decimal(18,4)' | YES | bytearray(b'') |



### s02_us_nahb_wells_fargo_national_hmi_history () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | value | b'decimal(18,4)' | YES | bytearray(b'') |



### s02_us_newyork_fed_inflation_expectations_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | Age40_60 | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | AgeOver_60 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | AgeUnder_40 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | YES | bytearray(b'') |
| 7 | EducationBA_or_Higher | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | EducationHighSchool_or_Less | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | EducationSomeCollege | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Income_50_100k | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Income_under_50k | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | IncomeOver_100k | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 12 | NumeracyHigh | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | NumeracyLow | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 19 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 14 | RegionMidwest | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | RegionNortheast | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | RegionSouth | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | RegionWest | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 17 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 22 | Updatetime | b'datetime' | YES | bytearray(b'') |



### s02_us_nonfarm_payrolls_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 2 | Nonfarm_payrolls_change | b'int(8)' | YES | bytearray(b'') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_nrp () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 30 | Change_in_Banks_Own_Net_Dollar_denom_Liabs | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Domes_LT_Secur_Purch_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Foreign_Bonds_Purch_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Foreign_Equity_Purch_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Foreign_LT_Secur_Purch_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Gross_Foreign_Purch_Foreign_LT_Secur_from_US | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_Foreign_Purch_of_Domes_US_LT_Secur | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Gross_Foreign_Sales_Foreign_LT_Secur_to_US | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Gross_Foreign_Sales_of_Domes_US_LT_Secur | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Increase_in_ForeignHoldings_of_Dollardenom_ST_US_S_O_C_L | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 31 | Monthly_Net_TIC_Flows | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Net_Foreign_Acquis_of_LT_Secur | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Net_LT_Secur_ransac | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Official_Corp_Bonds_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Official_Equity_Net | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Official_Gov_t_Agency_Bonds_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Official_net_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Official_net_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Official_net_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Official_net_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Official_Treas_Bonds_Notes_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 21 | Other_Acquis_LT_Secur_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Other_Negot_Instr_Select_Other_Liabs | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 8 | Private_Corp_Bonds_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Private_Equity_Net | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Private_Gov_t_Agency_Bonds_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Private_net_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Private_net_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Private_net_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Private_net_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Private_Treas_Bonds_Notes_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 34 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 39 | Updatetime | b'datetime' | YES | bytearray(b'') |
| 24 | US_Treas_Bills | b'decimal(18,4)' | YES | bytearray(b'') |



### s02_us_permits_cust () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | category | b'varchar(20)' | NO | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | In_structures_with_1unit | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | In_structures_with_2_to_4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | In_structures_with_5units | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 19 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 17 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 10 | RegionMidwest_1unit | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | RegionMidwestTotal | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | RegionNortheast_1unit | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | RegionNortheastTotal | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | RegionSouth_1unit | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | RegionSouthTotal | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | RegionWest_1unit | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | RegionWestTotal | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 15 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 3 | Total | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Updatetime | b'datetime' | YES | bytearray(b'') |



### s02_us_personal_income_and_expenses_monthly () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 37 | Addenda | b'decimal(18,4)' | YES | bytearray(b'') |
| 43 | Chained_dollars | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Compensation_of_employees | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Current_dollars | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 39 | Disposable_personal_income | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | E_c_f_e_p_a_i_f | b'decimal(18,4)' | YES | bytearray(b'Employer contributions for employee pension and insurance funds1') |
| 9 | Employer_contributions_for_government_social_insurance | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Equals_Disposable_personal_income | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Equals_Personal_saving | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Farm | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Government | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Government_social_benefits_to_persons | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Less_Contributions_for_government_social_insurance_domestic | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Less_Personal_current_taxes | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Less_Personal_outlays | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 21 | Medicaid | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Medicare3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Nonfarm | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 24 | Other | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Other_current_transfer_receipts_from_business_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | P_i_e_c_t_r_b_o_c_2_d | b'decimal(18,4)' | YES | bytearray(b'Personal_income_excluding_current_transfer_receipts_billions_of_chained_2009_dollars5') |
| 10 | P_i_w_i_v_a_c_c_a | b'decimal(18,4)' | YES | bytearray(b'Proprietors_income_with_inventory_valuation_and_capital_consumption_adjustments') |
| 41 | Per_capita | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 30 | Personal_consumption_expenditures | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Personal_current_transfer_payments | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Personal_current_transfer_receipts | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Personal_dividend_income | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Personal_income | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Personal_income_receipts_on_assets | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Personal_interest_income | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Personal_interest_payments4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Personal_saving_as_a_percentage_of_disposable_personal_income | b'decimal(18,4)' | YES | bytearray(b'') |
| 44 | Population_midperiod_thousands_6 | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Private_industries | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Rental_income_of_persons_with_capital_consumption_adjustment | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Social_security2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 45 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 7 | Supplements_to_wages_and_salaries | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | To_government | b'decimal(18,4)' | YES | bytearray(b'') |
| 34 | To_the_rest_of_the_world_net | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Total_billions_of_chained_dollars5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Unemployment_insurance | b'decimal(18,4)' | YES | bytearray(b'') |
| 50 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 23 | Veterans_benefits | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Wages_and_salaries | b'decimal(18,4)' | YES | bytearray(b'') |



### s02_us_policy_rate_d () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 5 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 8 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 6 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 2 | RESBME_ND | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | RESBMS_ND | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 4 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 9 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_ppi_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 12 | category | b'varchar(30)' | YES | bytearray(b'\xe5\x88\x86\xe7\xb1\xbb') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 6 | Energy | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Foods | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Goods_less_foods_and_energy | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 17 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 15 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | Services | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Services_less_trade_transportation_and_warehousing | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 13 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 2 | Total | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Total_less_foods_energy_and_trade_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Trade | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Transportation_and_warehousing | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_ppi_y () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 12 | category | b'varchar(30)' | YES | bytearray(b'\xe5\x88\x86\xe7\xb1\xbb') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 6 | Energy | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Foods | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Goods_less_foods_and_energy | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 17 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 15 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | Services | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Services_less_trade_transportation_and_warehousing | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 13 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 2 | Total | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Total_less_foods_energy_and_trade_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Trade | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Transportation_and_warehousing | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_price_index_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 15 | Change_in_private_inventories | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 5 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Federal | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Fixed_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Government_consumption_expenditures_and_gross_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Gross_private_domestic_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Intellectual_property_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 25 | National_defense | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Net_exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Nondefense | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Nonresidential | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 30 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 3 | Personal_consumption_expenditures | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Residential | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Services | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Services_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Services_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 28 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 27 | State_and_local | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Structures | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_price_index_y () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 15 | Change_in_private_inventories | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 5 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | Federal | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Fixed_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Government_consumption_expenditures_and_gross_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Gross_private_domestic_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Intellectual_property_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 25 | National_defense | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Net_exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | Nondefense | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Nonresidential | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 30 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 3 | Personal_consumption_expenditures | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Residential | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Services | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Services_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Services_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 28 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 27 | State_and_local | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Structures | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_r539cy () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | Continued_Claims_NSA | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Continued_Claims_SA | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Continued_Claims_SA_4_Week | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Continued_Claims_SF | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Covered_Employment | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 2 | Initial_Claims_NSA | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Initial_Claims_SA | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Initial_Claims_SA_4_Week | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Initial_Claims_SF | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | IUR_NSA | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | IUR_SA | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 17 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 15 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 16 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 13 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 18 | Updatetime | b'datetime' | YES | bytearray(b'') |



### s02_us_realgdp_a () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 43 | Change_in_private_inventories | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Clothing_and_footwear | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Computers_and_peripheral_equipment4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 56 | Consumption_expenditures_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 59 | Consumption_expenditures_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 62 | Consumption_expenditures_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 5 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | Entertainment_literary_and_artistic_originals | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | F_c_e_o_n_i_s_h_N | b'decimal(18,4)' | YES | bytearray(b'Final_consumption_expenditures_of_nonprofit_institutions_serving_households_NPISHs1') |
| 44 | Farm | b'decimal(18,4)' | YES | bytearray(b'') |
| 54 | Federal | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Financial_services_and_insurance | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Fixed_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Food_and_beverages_purchased_for_off_premises_consumption | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Food_services_and_accommodations | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Furnishings_and_durable_household_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Gasoline_and_other_energy_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 51 | Goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Government_consumption_expenditures_and_gross_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 57 | Gross_investment_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 60 | Gross_investment_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 63 | Gross_investment_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Gross_output_of_nonprofit_institutions2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Gross_private_domestic_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Health_care | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Household_consumption_expenditures_for_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Housing_and_utilities | b'decimal(18,4)' | YES | bytearray(b'') |
| 50 | Imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Industrial_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Information_processing_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Intellectual_property_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | L_R_f_s_o_g_a_s_b_n_i | b'decimal(18,4)' | YES | bytearray(b'Less_Receipts_from_sales_of_goods_and_services_by_nonprofit_institutions3') |
| 66 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 6 | Motor_vehicles_and_parts | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | National_defense | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Net_exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 58 | Nondefense | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Nonfarm | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Nonresidential | b'decimal(18,4)' | YES | bytearray(b'') |
| 69 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 34 | Other | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Other_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Other_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Other_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Other_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 67 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 3 | Personal_consumption_expenditures | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Recreation_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Recreational_goods_and_vehicles | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Research_and_development6 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Residential | b'decimal(18,4)' | YES | bytearray(b'') |
| 64 | Residual | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Services | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Services_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 52 | Services_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Software5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 68 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 65 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 61 | State_and_local | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Structures | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Transportation_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Transportation_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 70 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_realgdp_q () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 43 | Change_in_private_inventories | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | Clothing_and_footwear | b'decimal(18,4)' | YES | bytearray(b'') |
| 33 | Computers_and_peripheral_equipment4 | b'decimal(18,4)' | YES | bytearray(b'') |
| 56 | Consumption_expenditures_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 59 | Consumption_expenditures_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 62 | Consumption_expenditures_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 5 | Durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 41 | Entertainment_literary_and_artistic_originals | b'decimal(18,4)' | YES | bytearray(b'') |
| 31 | Equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 47 | Exports | b'decimal(18,4)' | YES | bytearray(b'') |
| 24 | F_c_e_o_n_i_s_h_N | b'decimal(18,4)' | YES | bytearray(b'Final_consumption_expenditures_of_nonprofit_institutions_serving_households_NPISHs1') |
| 44 | Farm | b'decimal(18,4)' | YES | bytearray(b'') |
| 54 | Federal | b'decimal(18,4)' | YES | bytearray(b'') |
| 22 | Financial_services_and_insurance | b'decimal(18,4)' | YES | bytearray(b'') |
| 28 | Fixed_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | Food_and_beverages_purchased_for_off_premises_consumption | b'decimal(18,4)' | YES | bytearray(b'') |
| 21 | Food_services_and_accommodations | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | Furnishings_and_durable_household_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Gasoline_and_other_energy_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Goods_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 48 | Goods_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 51 | Goods_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 53 | Government_consumption_expenditures_and_gross_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | Gross_domestic_product | b'decimal(18,4)' | YES | bytearray(b'') |
| 57 | Gross_investment_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 60 | Gross_investment_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 63 | Gross_investment_3 | b'decimal(18,4)' | YES | bytearray(b'') |
| 25 | Gross_output_of_nonprofit_institutions2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 27 | Gross_private_domestic_investment | b'decimal(18,4)' | YES | bytearray(b'') |
| 18 | Health_care | b'decimal(18,4)' | YES | bytearray(b'') |
| 16 | Household_consumption_expenditures_for_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 17 | Housing_and_utilities | b'decimal(18,4)' | YES | bytearray(b'') |
| 50 | Imports | b'decimal(18,4)' | YES | bytearray(b'') |
| 35 | Industrial_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 32 | Information_processing_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 38 | Intellectual_property_products | b'decimal(18,4)' | YES | bytearray(b'') |
| 26 | L_R_f_s_o_g_a_s_b_n_i | b'decimal(18,4)' | YES | bytearray(b'Less_Receipts_from_sales_of_goods_and_services_by_nonprofit_institutions3') |
| 66 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 6 | Motor_vehicles_and_parts | b'decimal(18,4)' | YES | bytearray(b'') |
| 55 | National_defense | b'decimal(18,4)' | YES | bytearray(b'') |
| 46 | Net_exports_of_goods_and_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 58 | Nondefense | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 45 | Nonfarm | b'decimal(18,4)' | YES | bytearray(b'') |
| 29 | Nonresidential | b'decimal(18,4)' | YES | bytearray(b'') |
| 69 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 34 | Other | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | Other_durable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 37 | Other_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 14 | Other_nondurable_goods | b'decimal(18,4)' | YES | bytearray(b'') |
| 23 | Other_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 67 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 3 | Personal_consumption_expenditures | b'decimal(18,4)' | YES | bytearray(b'') |
| 20 | Recreation_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Recreational_goods_and_vehicles | b'decimal(18,4)' | YES | bytearray(b'') |
| 40 | Research_and_development6 | b'decimal(18,4)' | YES | bytearray(b'') |
| 42 | Residential | b'decimal(18,4)' | YES | bytearray(b'') |
| 64 | Residual | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Services | b'decimal(18,4)' | YES | bytearray(b'') |
| 49 | Services_1 | b'decimal(18,4)' | YES | bytearray(b'') |
| 52 | Services_2 | b'decimal(18,4)' | YES | bytearray(b'') |
| 39 | Software5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 68 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 65 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 61 | State_and_local | b'decimal(18,4)' | YES | bytearray(b'') |
| 30 | Structures | b'decimal(18,4)' | YES | bytearray(b'') |
| 36 | Transportation_equipment | b'decimal(18,4)' | YES | bytearray(b'') |
| 19 | Transportation_services | b'decimal(18,4)' | YES | bytearray(b'') |
| 70 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_retail_sales_ym () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 68 | ADJUSTED_2 | b'decimal(18,4)' | YES | bytearray(b'ADJUSTED(2)') |
| 54 | All_other_gen_merchandise_stores_1 | b'decimal(18,4)' | YES | bytearray(b'All other gen. merchandise stores') |
| 101 | All_other_gen_merchandise_stores_2 | b'decimal(18,4)' | YES | bytearray(b'All other gen. merchandise stores') |
| 21 | All_other_home_furnishings_stores_1 | b'decimal(18,4)' | YES | bytearray(b'All other home furnishings stores') |
| 11 | Automobile_and_other_motor_vehicle_dealers_1 | b'decimal(18,4)' | YES | bytearray(b'Automobile and other motor vehicle dealers') |
| 77 | Automobile_and_other_motor_vehicle_dealers_2 | b'decimal(18,4)' | YES | bytearray(b'Automobile and other motor vehicle dealers') |
| 12 | Automobile_dealers_1 | b'decimal(18,4)' | YES | bytearray(b'Automobile dealers') |
| 15 | Automotive_parts_acc_1and_tire_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Automotive parts, acc., and tire stores') |
| 78 | Automotive_parts_acc_and_tire_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Automotive parts, acc., and tire stores') |
| 32 | Beer_wine_and_liquor_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Beer, wine, and liquor stores') |
| 86 | Beer_wine_and_liquor_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Beer, wine and liquor stores') |
| 47 | Book_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Book stores') |
| 25 | Building_mat_and_garden_equip_and_supplies_dealers_1 | b'decimal(18,4)' | YES | bytearray(b'Building mat. and garden equip. and supplies dealers') |
| 82 | Building_mat_and_garden_equip_and_supplies_dealers_2 | b'decimal(18,4)' | YES | bytearray(b'Building mat. and garden equip. and supplies dealers') |
| 26 | Building_mat_and_supplies_dealers_1 | b'decimal(18,4)' | YES | bytearray(b'Building mat. and supplies dealers') |
| 83 | Building_mat_and_supplies_dealers_2 | b'decimal(18,4)' | YES | bytearray(b'Building mat. and supplies dealers') |
| 36 | Clothing_and_clothing_access_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Clothing and clothing access. stores') |
| 90 | Clothing_and_clothing_access_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Clothing and clothing access. stores') |
| 37 | Clothing_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Clothing stores') |
| 91 | Clothing_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Clothing stores') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 49 | Department_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Department stores') |
| 98 | Department_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Department stores') |
| 50 | Department_stores_excl_discount_department_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Department stores(excl. discount department stores)') |
| 51 | Discount_dept_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Discount dept. stores') |
| 64 | Drinking_places_1 | b'decimal(18,4)' | YES | bytearray(b'Drinking places') |
| 61 | Electronic_shopping_and_mail_order_houses_1 | b'decimal(18,4)' | YES | bytearray(b'Electronic shopping and mail-order houses') |
| 104 | Electronic_shopping_and_mail_order_houses_2 | b'decimal(18,4)' | YES | bytearray(b'Electronic shopping and mail order houses') |
| 22 | Electronics_and_appliance_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Electronics and appliance stores') |
| 81 | Electronics_and_appliance_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Electronics and appliance stores') |
| 24 | Electronics_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Electronics stores') |
| 40 | Family_clothing_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Family clothing stores') |
| 20 | Floor_covering_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Floor covering stores') |
| 29 | Food_and_beverage_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Food and beverage stores') |
| 84 | Food_and_beverage_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Food and beverage stores') |
| 63 | Food_services_and_drinking_places_1 | b'decimal(18,4)' | YES | bytearray(b'Food services and drinking places') |
| 106 | Food_services_and_drinking_places_2 | b'decimal(18,4)' | YES | bytearray(b'Food services and drinking places') |
| 62 | Fuel_dealers_1 | b'decimal(18,4)' | YES | bytearray(b'Fuel dealers') |
| 105 | Fuel_dealers_2 | b'decimal(18,4)' | YES | bytearray(b'Fuel dealers') |
| 66 | Full_service_restaurants_1 | b'decimal(18,4)' | YES | bytearray(b'Full service restaurants') |
| 17 | Furniture_and_home_furnishings_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Furniture and home furnishings stores') |
| 80 | Furniture_and_home_furnishings_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Furniture and home furnishings stores') |
| 16 | Furniture_home_furn_electronics_and_appliance_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Furniture, home furn, electronics, and appliance stores') |
| 79 | Furniture_home_furn_electronics_and_appliance_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Furniture, home furn, electronics, and appliance stores') |
| 18 | Furniture_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Furniture stores') |
| 9 | GAFO_1 | b'decimal(18,4)' | YES | bytearray(b'GAFO(1)') |
| 75 | GAFO_2 | b'decimal(18,4)' | YES | bytearray(b'GAFO(1)') |
| 35 | Gasoline_stations_1 | b'decimal(18,4)' | YES | bytearray(b'Gasoline stations') |
| 89 | Gasoline_stations_2 | b'decimal(18,4)' | YES | bytearray(b'Gasoline stations') |
| 48 | General_merchandise_stores_1 | b'decimal(18,4)' | YES | bytearray(b'General merchandise stores') |
| 97 | General_merchandise_stores_2 | b'decimal(18,4)' | YES | bytearray(b'General merchandise stores') |
| 58 | Gift_novelty_and_souvenir_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Gift, novelty, and souvenir stores') |
| 30 | Grocery_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Grocery stores') |
| 85 | Grocery_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Grocery stores') |
| 28 | Hardware_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Hardware stores') |
| 33 | Health_and_personal_care_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Health and personal care stores') |
| 87 | Health_and_personal_care_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Health and personal care stores') |
| 46 | Hobby_toy_and_game_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Hobby, toy, and game stores') |
| 19 | Home_furnishings_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Home furnishings stores') |
| 23 | Household_appliance_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Household appliance stores') |
| 43 | Jewelry_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Jewelry stores') |
| 95 | Jewelry_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Jewelry stores') |
| 67 | Limited_service_eating_places_1 | b'decimal(18,4)' | YES | bytearray(b'Limited service eating places') |
| 108 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 38 | Mens_clothing_stores_1 | b'decimal(18,4)' | YES | bytearray(b"Men\'s clothing stores") |
| 92 | Mens_clothing_stores_2 | b'decimal(18,4)' | YES | bytearray(b"Men\'s clothing stores") |
| 55 | Miscellaneous_store_retailers_1 | b'decimal(18,4)' | YES | bytearray(b'Miscellaneous store retailers') |
| 102 | Miscellaneous_stores_retailers_2 | b'decimal(18,4)' | YES | bytearray(b'Miscellaneous stores retailers') |
| 10 | Motor_vehicle_and_parts_dealers | b'decimal(18,4)' | YES | bytearray(b'Motor vehicle and parts dealers') |
| 76 | Motor_vehicle_and_parts_dealers_2 | b'decimal(18,4)' | YES | bytearray(b'Motor vehicle and parts dealers') |
| 13 | New_car_dealers_1 | b'decimal(18,4)' | YES | bytearray(b'New car dealers') |
| 60 | Nonstore_retailers_1 | b'decimal(18,4)' | YES | bytearray(b'Nonstore retailers') |
| 103 | Nonstore_retailers_2 | b'decimal(18,4)' | YES | bytearray(b'Nonstore retailers') |
| 2 | NOT_ADJUSTED | b'decimal(18,4)' | YES | bytearray(b'NOT ADJUSTED') |
| 57 | Office_supplies_and_stationery_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Office supplies and stationery stores') |
| 56 | Office_supplies_stationery_and_gift_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Office supplies, stationery, and gift stores') |
| 111 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 41 | Other_clothing_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Other clothing stores') |
| 52 | Other_general_merchandise_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Other general merchandise stores') |
| 99 | Other_general_merchandise_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Other general merchandise stores') |
| 27 | Paint_and_wallpaper_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Paint and wallpaper stores') |
| 109 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 34 | Pharmacies_and_drug_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Pharmacies and drug stores') |
| 88 | Pharmacies_and_drug_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Pharmacies and drug stores') |
| 72 | R_s_and_f_s_e_motor_v_and_parts_and_gasoline_s_2 | b'decimal(18,4)' | YES | bytearray(b'Retail sales and food services excl motor vehicle and parts and gasoline stations') |
| 71 | R_s_and_f_s_excl_gasoline_stations_2 | b'decimal(18,4)' | YES | bytearray(b'Retail sales and food services excl gasoline stations') |
| 6 | R_s_and_f_s_excl_motor_v_and_parts_and_gasoline_s_1 | b'decimal(18,4)' | YES | bytearray(b'Retail sales and food services excl motor vehicle and parts and gasoline stations') |
| 4 | R_s_and_f_s_excl_motor_vehicle_and_parts_1 | b'decimal(18,4)' | YES | bytearray(b'Retail sales and food services excl motor vehicle and parts') |
| 70 | R_s_and_f_s_excl_motor_vehicle_and_parts_2 | b'decimal(18,4)' | YES | bytearray(b'Retail sales and food services excl motor vehicle and parts') |
| 8 | R_s_t_excl_motor_vehicle_and_parts_dealers | b'decimal(18,4)' | YES | bytearray(b'Retail sales, total (excl. motor vehicle and parts dealers)') |
| 74 | R_s_total_excl_motor_vehicle_and_parts_dealers_2 | b'decimal(18,4)' | YES | bytearray(b'Retail sales, total (excl. motor vehicle and parts dealers)') |
| 65 | Restaurants_and_other_eating_places_1 | b'decimal(18,4)' | YES | bytearray(b'Restaurants and other eating places') |
| 3 | Retail_and_food_services_sales_total_1 | b'decimal(18,4)' | YES | bytearray(b'Retail and food services sales, total') |
| 69 | Retail_and_food_services_sales_total_2 | b'decimal(18,4)' | YES | bytearray(b'Retail and food services sales, total') |
| 5 | Retail_sales_and_food_services_excl_gasoline_stations_1 | b'decimal(18,4)' | YES | bytearray(b'Retail sales and food services excl gasoline stations') |
| 7 | Retail_sales_total | b'decimal(18,4)' | YES | bytearray(b'Retail sales, total') |
| 73 | Retail_sales_total_2 | b'decimal(18,4)' | YES | bytearray(b'Retail sales, total') |
| 42 | Shoe_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Shoe stores') |
| 94 | Shoe_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Shoe stores') |
| 110 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 107 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 44 | Sporting_goods_hobby_musical_instrument_and_book_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Sporting goods, hobby, musical instrument, and book stores') |
| 96 | Sporting_goods_hobby_musical_instrument_and_book_stores_2 | b'decimal(18,4)' | YES | bytearray(b'Sporting goods, hobby, musical instrument, and book stores') |
| 45 | Sporting_goods_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Sporting goods stores') |
| 31 | Supermarkets_and_other_grocery_except_convenience_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Supermarkets and other grocery (except convenience) stores') |
| 112 | Updatetime | b'datetime' | YES | bytearray(b'') |
| 14 | Used_car_dealers_1 | b'decimal(18,4)' | YES | bytearray(b'Used car dealers') |
| 59 | Used_merchandise_stores_1 | b'decimal(18,4)' | YES | bytearray(b'Used merchandise stores') |
| 53 | Warehouse_clubs_and_superstores_1 | b'decimal(18,4)' | YES | bytearray(b'Warehouse clubs and superstores') |
| 100 | Warehouse_clubs_and_superstores_2 | b'decimal(18,4)' | YES | bytearray(b'Warehouse clubs and superstores') |
| 39 | Womens_clothing_stores_1 | b'decimal(18,4)' | YES | bytearray(b"Women\'s clothing stores") |
| 93 | Womens_clothing_stores_2 | b'decimal(18,4)' | YES | bytearray(b"Women\'s clothing stores") |



### s02_us_stage_cust () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | category | b'varchar(20)' | NO | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 10 | For_Sale_at_end_of_period_Completed | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | For_Sale_at_end_of_period_Median_Numberof_monthsfor_sale | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | For_Sale_at_end_of_period_NotStarted | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | For_Sale_at_end_of_period_Total | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | For_Sale_at_end_of_period_UnderConstruction | b'decimal(18,4)' | YES | bytearray(b'') |
| 13 | Measurment | b'varchar(20)' | YES | bytearray(b'') |
| 16 | Organization | b'varchar(50)' | YES | bytearray(b'') |
| 14 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 6 | Sold_during_period_Competed | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | Sold_during_period_NotStarted | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | Sold_during_period_Total | b'decimal(18,4)' | YES | bytearray(b'') |
| 5 | Sold_during_period_UnderConstruction | b'decimal(18,4)' | YES | bytearray(b'') |
| 15 | Source | b'varchar(50)' | YES | bytearray(b'') |
| 12 | Species | b'varchar(30)' | YES | bytearray(b'') |
| 17 | Updatetime | b'datetime' | YES | bytearray(b'') |



### s02_us_underlying_inflation_gauge_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | CPI_inflation | b'decimal(18,4)' | YES | bytearray(b'') |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 6 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 9 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 8 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 5 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 2 | UIG_Full_data_set_measure | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | UIG_Prices_only_measure | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_us_unemployment_rate_m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Datetime | b'datetime' | NO | bytearray(b'') |
| 4 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe5\x80\xbc\xe7\x9a\x84\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |
| 7 | Organization | b'varchar(50)' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x8d\x95\xe4\xbd\x8d') |
| 5 | Period | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe9\xa2\x91\xe5\xba\xa6') |
| 6 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 3 | Species | b'varchar(30)' | YES | bytearray(b'\xe6\xb3\xa8\xe6\x98\x8e\xe8\xaf\xa5\xe6\x8c\x87\xe6\xa0\x87\xe7\x9a\x84\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe6\xb3\x95') |
| 2 | Unemployment_rate | b'decimal(18,4)' | YES | bytearray(b'') |
| 8 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s02_user_comment () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | date | b'datetime(6)' | NO | bytearray(b'') |
| 5 | file | b'varchar(200)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 3 | usercomment | b'longtext' | NO | bytearray(b'') |
| 2 | username | b'varchar(100)' | NO | bytearray(b'') |



### s02_user_out_company () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 5 | invited_code | b'varchar(100)' | NO | bytearray(b'') |
| 7 | power_level | b'varchar(3)' | NO | bytearray(b'') |
| 6 | powerOff | b'datetime(6)' | NO | bytearray(b'') |
| 4 | userId | b'int(11)' | NO | bytearray(b'') |
| 3 | userinfo | b'varchar(100)' | NO | bytearray(b'') |
| 2 | username | b'varchar(100)' | NO | bytearray(b'') |



### s02_user_sycapital_user () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 13 | creat_date | b'datetime(6)' | NO | bytearray(b'') |
| 9 | Email | b'varchar(30)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 6 | invite_code | b'varchar(100)' | NO | bytearray(b'') |
| 7 | invited_code | b'varchar(100)' | NO | bytearray(b'') |
| 11 | Job | b'varchar(30)' | NO | bytearray(b'') |
| 10 | PartOf | b'varchar(30)' | NO | bytearray(b'') |
| 4 | password | b'varchar(25)' | NO | bytearray(b'') |
| 8 | PhoneNum | b'varchar(13)' | NO | bytearray(b'') |
| 12 | power_level | b'varchar(100)' | NO | bytearray(b'') |
| 14 | up_date | b'datetime(6)' | NO | bytearray(b'') |
| 2 | user | b'varchar(10)' | NO | bytearray(b'') |
| 5 | user_ID | b'int(11)' | NO | bytearray(b'') |
| 3 | username | b'varchar(10)' | NO | bytearray(b'') |



### s02_user_sycapital_user_test () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 13 | creat_date | b'datetime(6)' | NO | bytearray(b'') |
| 9 | Email | b'varchar(30)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 6 | invite_code | b'varchar(100)' | NO | bytearray(b'') |
| 7 | invited_code | b'varchar(100)' | NO | bytearray(b'') |
| 11 | Job | b'varchar(30)' | NO | bytearray(b'') |
| 10 | PartOf | b'varchar(30)' | NO | bytearray(b'') |
| 4 | password | b'varchar(25)' | NO | bytearray(b'') |
| 8 | PhoneNum | b'varchar(13)' | NO | bytearray(b'') |
| 12 | power_level | b'varchar(100)' | NO | bytearray(b'') |
| 14 | up_date | b'datetime(6)' | NO | bytearray(b'') |
| 2 | user | b'varchar(10)' | NO | bytearray(b'') |
| 5 | user_ID | b'int(11)' | NO | bytearray(b'') |
| 3 | username | b'varchar(10)' | NO | bytearray(b'') |



### s02_user_user_session () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 3 | Session_ID | b'varchar(50)' | NO | bytearray(b'') |
| 4 | UpDate | b'datetime(6)' | NO | bytearray(b'') |
| 2 | UserName | b'varchar(10)' | NO | bytearray(b'') |



### s02_yanbao_yanbao () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | author | b'varchar(10)' | NO | bytearray(b'') |
| 8 | biaoqian | b'varchar(50)' | NO | bytearray(b'') |
| 3 | date_time | b'datetime(6)' | NO | bytearray(b'') |
| 4 | fileName | b'varchar(50)' | NO | bytearray(b'') |
| 5 | filePath | b'varchar(100)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 9 | level | b'varchar(20)' | NO | bytearray(b'') |
| 10 | page | b'int(11)' | NO | bytearray(b'') |
| 6 | refer | b'varchar(50)' | NO | bytearray(b'') |
| 2 | title | b'varchar(200)' | NO | bytearray(b'') |
| 11 | update | b'datetime(6)' | NO | bytearray(b'') |



### s03_ged_code_data () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | begin_date | b'datetime' | YES | bytearray(b'\xe8\xb5\xb7\xe5\xa7\x8b\xe6\x97\xa5\xe6\x9c\x9f') |
| 9 | create_time | b'datetime' | YES | bytearray(b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4') |
| 6 | data_value | b'decimal(28,6)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe6\x8d\xae') |
| 5 | end_date | b'datetime' | YES | bytearray(b'\xe6\x88\xaa\xe8\x87\xb3\xe6\x97\xa5\xe6\x9c\x9f') |
| 1 | id | b'int(11)' | NO | bytearray(b'\xe8\x87\xaa\xe5\xa2\x9eID') |
| 3 | info_publdate | b'datetime' | YES | bytearray(b'\xe4\xbf\xa1\xe6\x81\xaf\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f') |
| 8 | modified_time | b'datetime' | YES | bytearray(b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | node_code | b'bigint(20)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe4\xbb\xa3\xe7\xa0\x81') |
| 7 | power_number | b'int(11)' | YES | bytearray(b'\xe9\x87\x8f\xe7\xba\xb2\xe7\xb3\xbb\xe6\x95\xb0') |



### s03_ged_middle_tree () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | create_time | b'datetime' | YES | bytearray(b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4') |
| 1 | id | b'int(11)' | NO | bytearray(b'\xe8\x87\xaa\xe5\xa2\x9eID') |
| 3 | jy_node | b'bigint(20)' | YES | bytearray(b'\xe8\x81\x9a\xe6\xba\x90\xe4\xbb\xa3\xe7\xa0\x81') |
| 5 | modified_time | b'datetime' | YES | bytearray(b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4') |
| 4 | node_category | b'tinyint(3)' | YES | bytearray(b'1-\xe5\xad\x97\xe8\x8a\x82\xe7\x82\xb9\xef\xbc\x8c2-\xe5\x8f\xb6\xe8\x8a\x82\xe7\x82\xb9') |
| 2 | sy_node | b'bigint(20)' | YES | bytearray(b'\xe7\x86\xb5\xe4\xb8\x80\xe4\xbb\xa3\xe7\xa0\x81') |



### s03_ged_node_main () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | begin_date | b'datetime' | YES | bytearray(b'\xe8\xb5\xb7\xe5\xa7\x8b\xe6\x97\xa5\xe6\x9c\x9f') |
| 6 | create_time | b'datetime' | YES | bytearray(b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4') |
| 10 | disclosure_frequency | b'int(11)' | YES | bytearray(b'\xe6\x8a\xab\xe9\x9c\xb2\xe9\xa2\x91\xe7\x8e\x87') |
| 8 | end_date | b'datetime' | YES | bytearray(b'\xe6\x97\xa5\xe6\x9c\x9f') |
| 1 | id | b'int(11)' | NO | bytearray(b'id') |
| 5 | modified_time | b'datetime' | YES | bytearray(b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | node_code | b'bigint(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | node_name | b'varchar(300)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe5\x90\x8d\xe7\xa7\xb0') |
| 4 | node_status | b'tinyint(3)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe7\x8a\xb6\xe6\x80\x81') |
| 11 | remarks | b'varchar(2000)' | YES | bytearray(b'\xe5\xa4\x87\xe6\xb3\xa8') |
| 9 | unit_code | b'int(11)' | YES | bytearray(b'\xe8\xae\xa1\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |



### s03_ged_node_tree () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | brother_number | b'int(5)' | YES | bytearray(b'\xe5\x85\x84\xe5\xbc\x9f\xe6\x8e\x92\xe5\xba\x8f') |
| 10 | create_time | b'datetime' | YES | bytearray(b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4') |
| 1 | id | b'int(11)' | NO | bytearray(b'id') |
| 6 | level_number | b'tinyint(3)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe6\xb7\xb1\xe5\xba\xa6') |
| 9 | modified_time | b'datetime' | YES | bytearray(b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4') |
| 7 | node_category | b'tinyint(3)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe7\xb1\xbb\xe5\x9e\x8b') |
| 2 | node_code | b'bigint(20)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | node_name | b'varchar(300)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe5\x90\x8d\xe7\xa7\xb0') |
| 8 | node_status | b'tinyint(3)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe7\x8a\xb6\xe6\x80\x81') |
| 4 | parent_node | b'bigint(20)' | YES | bytearray(b'\xe7\x88\xb6\xe8\x8a\x82\xe7\x82\xb9\xe4\xbb\xa3\xe7\xa0\x81') |



### s03_ged_system_const () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | const_code | b'int(11)' | YES | bytearray(b'\xe5\xb8\xb8\xe9\x87\x8f\xe4\xbb\xa3\xe7\xa0\x81') |
| 5 | const_description | b'varchar(300)' | YES | bytearray(b'\xe5\xb8\xb8\xe9\x87\x8f\xe6\x8f\x8f\xe8\xbf\xb0') |
| 6 | const_parent_code | b'bigint(11)' | YES | bytearray(b'\xe5\xb8\xb8\xe9\x87\x8f\xe7\x88\xb6\xe7\xba\xa7\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | const_sort_code | b'int(11)' | YES | bytearray(b'\xe5\xb8\xb8\xe9\x87\x8f\xe5\x88\x86\xe7\xb1\xbb\xe7\xbc\x96\xe7\xa0\x81') |
| 3 | const_sort_name | b'varchar(100)' | YES | bytearray(b'\xe5\xb8\xb8\xe9\x87\x8f\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0') |
| 12 | create_time | b'datetime' | YES | bytearray(b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4') |
| 10 | cvalue | b'varchar(500)' | YES | bytearray(b'\xe9\xa2\x84\xe7\x95\x99\xe6\xa0\x87\xe5\xbf\x97\xe4\xbd\x8d(\xe5\xad\x97\xe7\xac\xa6\xe5\x80\xbc)') |
| 9 | dvalue | b'datetime' | YES | bytearray(b'\xe9\xa2\x84\xe7\x95\x99\xe6\xa0\x87\xe5\xbf\x97\xe4\xbd\x8d(\xe6\x97\xa5\xe6\x9c\x9f\xe5\x80\xbc)') |
| 8 | fvalue | b'float' | YES | bytearray(b'\xe9\xa2\x84\xe7\x95\x99\xe6\xa0\x87\xe5\xbf\x97\xe4\xbd\x8d(\xe6\xb5\xae\xe7\x82\xb9\xe5\x80\xbc)') |
| 1 | id | b'int(11)' | NO | bytearray(b'id') |
| 7 | ivalue | b'int(11)' | YES | bytearray(b'\xe9\xa2\x84\xe7\x95\x99\xe6\xa0\x87\xe5\xbf\x97\xe4\xbd\x8d(\xe6\x95\xb4\xe5\xbd\xa2\xe5\x80\xbc)') |
| 11 | modified_time | b'datetime' | YES | bytearray(b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4') |



### s03_indicator_code_data () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | begin_date | b'datetime' | YES | bytearray(b'\xe8\xb5\xb7\xe5\xa7\x8b\xe6\x97\xa5\xe6\x9c\x9f') |
| 9 | create_time | b'datetime' | YES | bytearray(b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4') |
| 6 | data_value | b'decimal(28,6)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe6\x8d\xae') |
| 5 | end_date | b'datetime' | YES | bytearray(b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f') |
| 1 | id | b'int(11)' | NO | bytearray(b'\xe8\x87\xaa\xe5\xa2\x9eID') |
| 3 | info_publdate | b'datetime' | YES | bytearray(b'\xe4\xbf\xa1\xe6\x81\xaf\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f') |
| 10 | jy_time | b'datetime' | YES | bytearray(b'\xe8\x81\x9a\xe6\xba\x90\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 8 | modified_time | b'datetime' | YES | bytearray(b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | node_code | b'bigint(20)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe4\xbb\xa3\xe7\xa0\x81') |
| 7 | power_number | b'int(11)' | YES | bytearray(b'\xe9\x87\x8f\xe7\xba\xb2\xe7\xb3\xbb\xe6\x95\xb0') |



### s03_indicator_node_main () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | begin_date | b'datetime' | YES | bytearray(b'\xe8\xb5\xb7\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4') |
| 6 | create_time | b'datetime' | YES | bytearray(b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4') |
| 10 | disclosure_frequency | b'int(11)' | YES | bytearray(b'\xe6\x8a\xab\xe9\x9c\xb2\xe9\xa2\x91\xe7\x8e\x87') |
| 8 | end_date | b'datetime' | YES | bytearray(b'\xe6\x97\xa5\xe6\x9c\x9f') |
| 1 | id | b'int(11)' | NO | bytearray(b'id') |
| 12 | jy_time | b'datetime' | YES | bytearray(b'\xe8\x81\x9a\xe6\xba\x90\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 5 | modified_time | b'datetime' | YES | bytearray(b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | node_code | b'bigint(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | node_name | b'varchar(300)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe5\x90\x8d\xe7\xa7\xb0') |
| 4 | node_status | b'tinyint(3)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe7\x8a\xb6\xe6\x80\x81') |
| 11 | remarks | b'varchar(2000)' | YES | bytearray(b'\xe5\xa4\x87\xe6\xb3\xa8') |
| 9 | unit_code | b'int(11)' | YES | bytearray(b'\xe8\xae\xa1\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |



### s03_indicator_node_tree () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | brother_number | b'int(5)' | YES | bytearray(b'\xe5\x85\x84\xe5\xbc\x9f\xe6\x8e\x92\xe5\xba\x8f') |
| 10 | create_time | b'datetime' | YES | bytearray(b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4') |
| 1 | id | b'int(11)' | NO | bytearray(b'id') |
| 11 | JSID | b'bigint(20)' | YES | bytearray(b'JSID') |
| 12 | jy_time | b'datetime' | YES | bytearray(b'\xe8\x81\x9a\xe6\xba\x90\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 6 | level_number | b'tinyint(3)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe6\xb7\xb1\xe5\xba\xa6') |
| 9 | modified_time | b'datetime' | YES | bytearray(b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4') |
| 7 | node_category | b'tinyint(3)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe7\xb1\xbb\xe5\x9e\x8b') |
| 2 | node_code | b'bigint(20)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | node_name | b'varchar(300)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe5\x90\x8d\xe7\xa7\xb0') |
| 8 | node_status | b'tinyint(3)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe7\x8a\xb6\xe6\x80\x81') |
| 4 | parent_node | b'bigint(20)' | YES | bytearray(b'\xe7\x88\xb6\xe8\x8a\x82\xe7\x82\xb9\xe4\xbb\xa3\xe7\xa0\x81') |



### s03_indicator_system_const () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | const_code | b'int(11)' | YES | bytearray(b'\xe5\xb8\xb8\xe9\x87\x8f\xe4\xbb\xa3\xe7\xa0\x81') |
| 5 | const_description | b'varchar(300)' | YES | bytearray(b'\xe5\xb8\xb8\xe9\x87\x8f\xe6\x8f\x8f\xe8\xbf\xb0') |
| 6 | const_parent_code | b'bigint(11)' | YES | bytearray(b'\xe5\xb8\xb8\xe9\x87\x8f\xe7\x88\xb6\xe7\xba\xa7\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | const_sort_code | b'int(11)' | YES | bytearray(b'\xe5\xb8\xb8\xe9\x87\x8f\xe5\x88\x86\xe7\xb1\xbb\xe7\xbc\x96\xe7\xa0\x81') |
| 3 | const_sort_name | b'varchar(100)' | YES | bytearray(b'\xe5\xb8\xb8\xe9\x87\x8f\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0') |
| 12 | create_time | b'datetime' | YES | bytearray(b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4') |
| 10 | cvalue | b'varchar(500)' | YES | bytearray(b'\xe9\xa2\x84\xe7\x95\x99\xe6\xa0\x87\xe5\xbf\x97\xe4\xbd\x8d(\xe5\xad\x97\xe7\xac\xa6\xe5\x80\xbc)') |
| 9 | dvalue | b'datetime' | YES | bytearray(b'\xe9\xa2\x84\xe7\x95\x99\xe6\xa0\x87\xe5\xbf\x97\xe4\xbd\x8d(\xe6\x97\xa5\xe6\x9c\x9f\xe5\x80\xbc)') |
| 8 | fvalue | b'float' | YES | bytearray(b'\xe9\xa2\x84\xe7\x95\x99\xe6\xa0\x87\xe5\xbf\x97\xe4\xbd\x8d(\xe6\xb5\xae\xe7\x82\xb9\xe5\x80\xbc)') |
| 1 | id | b'int(11)' | NO | bytearray(b'id') |
| 7 | ivalue | b'int(11)' | YES | bytearray(b'\xe9\xa2\x84\xe7\x95\x99\xe6\xa0\x87\xe5\xbf\x97\xe4\xbd\x8d(\xe6\x95\xb4\xe5\xbd\xa2\xe5\x80\xbc)') |
| 13 | jy_time | b'datetime' | YES | bytearray(b'\xe8\x81\x9a\xe6\xba\x90\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 11 | modified_time | b'datetime' | YES | bytearray(b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4') |



### s03_macro_code_data () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | begin_date | b'datetime' | YES | bytearray(b'\xe8\xb5\xb7\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4') |
| 9 | create_time | b'datetime' | YES | bytearray(b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4') |
| 6 | data_value | b'decimal(28,6)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe6\x8d\xae') |
| 5 | end_date | b'datetime' | YES | bytearray(b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f') |
| 1 | id | b'int(11)' | NO | bytearray(b'id') |
| 3 | info_publdate | b'datetime' | YES | bytearray(b'\xe4\xbf\xa1\xe6\x81\xaf\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4') |
| 10 | jy_time | b'datetime' | YES | bytearray(b'\xe8\x81\x9a\xe6\xba\x90\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 8 | modified_time | b'datetime' | YES | bytearray(b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4') |
| 2 | node_code | b'bigint(20)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe4\xbb\xa3\xe7\xa0\x81') |
| 7 | power_number | b'int(11)' | YES | bytearray(b'\xe9\x87\x8f\xe7\xba\xb2\xe7\xb3\xbb\xe6\x95\xb0') |



### s03_macro_middle_tree () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | create_time | b'datetime' | YES | bytearray(b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4') |
| 1 | id | b'int(11)' | NO | bytearray(b'\xe8\x87\xaa\xe5\xa2\x9eID') |
| 3 | jy_node | b'bigint(20)' | YES | bytearray(b'\xe8\x81\x9a\xe6\xba\x90\xe4\xbb\xa3\xe7\xa0\x81') |
| 5 | modified_time | b'datetime' | YES | bytearray(b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4') |
| 4 | node_category | b'tinyint(3)' | YES | bytearray(b'1-\xe5\xad\x97\xe8\x8a\x82\xe7\x82\xb9\xef\xbc\x8c2-\xe5\x8f\xb6\xe8\x8a\x82\xe7\x82\xb9') |
| 2 | sy_node | b'bigint(20)' | YES | bytearray(b'\xe7\x86\xb5\xe4\xb8\x80\xe4\xbb\xa3\xe7\xa0\x81') |



### s03_macro_node_main () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 11 | begin_date | b'datetime' | YES | bytearray(b'\xe8\xb5\xb7\xe5\xa7\x8b\xe6\x97\xa5\xe6\x9c\x9f') |
| 5 | brother_number | b'int(5)' | YES | bytearray(b'\xe5\x85\x84\xe5\xbc\x9f\xe6\x8e\x92\xe5\xba\x8f') |
| 10 | create_time | b'datetime' | YES | bytearray(b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4') |
| 14 | disclosure_frequency | b'int(11)' | YES | bytearray(b'\xe6\x89\xb9\xe9\x87\x8f\xe9\xa2\x91\xe7\x8e\x87') |
| 12 | end_date | b'datetime' | YES | bytearray(b'\xe6\x97\xa5\xe6\x9c\x9f') |
| 1 | id | b'int(11)' | NO | bytearray(b'id') |
| 16 | jy_time | b'datetime' | YES | bytearray(b'\xe8\x81\x9a\xe6\xba\x90\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 6 | level_number | b'tinyint(3)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe6\xb7\xb1\xe5\xba\xa6') |
| 9 | modified_time | b'datetime' | YES | bytearray(b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4') |
| 7 | node_category | b'tinyint(3)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe7\xb1\xbb\xe5\x9e\x8b') |
| 2 | node_code | b'bigint(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | node_name | b'varchar(300)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe5\x90\x8d\xe7\xa7\xb0') |
| 8 | node_status | b'tinyint(3)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe7\x8a\xb6\xe6\x80\x81') |
| 4 | parent_node | b'bigint(20)' | YES | bytearray(b'\xe7\x88\xb6\xe8\x8a\x82\xe7\x82\xb9\xe5\x90\x8d\xe7\xa7\xb0') |
| 15 | remarks | b'varchar(2000)' | YES | bytearray(b'\xe5\xa4\x87\xe6\xb3\xa8') |
| 13 | unit_code | b'int(11)' | YES | bytearray(b'\xe8\xae\xa1\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d') |



### s03_macro_node_tree () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | brother_number | b'int(5)' | YES | bytearray(b'\xe5\x85\x84\xe5\xbc\x9f\xe6\x8e\x92\xe5\xba\x8f') |
| 10 | create_time | b'datetime' | YES | bytearray(b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4') |
| 1 | id | b'int(11)' | NO | bytearray(b'id') |
| 11 | jy_time | b'datetime' | YES | bytearray(b'\xe8\x81\x9a\xe6\xba\x90\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 6 | level_number | b'tinyint(3)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe6\xb7\xb1\xe5\xba\xa6') |
| 9 | modified_time | b'datetime' | YES | bytearray(b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4') |
| 7 | node_category | b'tinyint(3)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe7\xb1\xbb\xe5\x9e\x8b') |
| 2 | node_code | b'bigint(20)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | node_name | b'varchar(300)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe5\x90\x8d\xe7\xa7\xb0') |
| 8 | node_status | b'tinyint(3)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe7\x8a\xb6\xe6\x80\x81') |
| 4 | parent_node | b'bigint(20)' | YES | bytearray(b'\xe7\x88\xb6\xe8\x8a\x82\xe7\x82\xb9\xe4\xbb\xa3\xe7\xa0\x81') |



### s03_macro_system_const () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | const_code | b'int(11)' | YES | bytearray(b'\xe5\xb8\xb8\xe9\x87\x8f\xe4\xbb\xa3\xe7\xa0\x81') |
| 5 | const_description | b'varchar(300)' | YES | bytearray(b'\xe5\xb8\xb8\xe9\x87\x8f\xe6\x8f\x8f\xe8\xbf\xb0') |
| 6 | const_parent_code | b'bigint(11)' | YES | bytearray(b'\xe5\xb8\xb8\xe9\x87\x8f\xe7\x88\xb6\xe7\xba\xa7\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | const_sort_code | b'int(11)' | YES | bytearray(b'\xe5\xb8\xb8\xe9\x87\x8f\xe5\x88\x86\xe7\xb1\xbb\xe7\xbc\x96\xe7\xa0\x81') |
| 3 | const_sort_name | b'varchar(100)' | YES | bytearray(b'\xe5\xb8\xb8\xe9\x87\x8f\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0') |
| 12 | create_time | b'datetime' | YES | bytearray(b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4') |
| 10 | cvalue | b'varchar(500)' | YES | bytearray(b'\xe9\xa2\x84\xe7\x95\x99\xe6\xa0\x87\xe5\xbf\x97\xe4\xbd\x8d(\xe5\xad\x97\xe7\xac\xa6\xe5\x80\xbc)') |
| 9 | dvalue | b'datetime' | YES | bytearray(b'\xe9\xa2\x84\xe7\x95\x99\xe6\xa0\x87\xe5\xbf\x97\xe4\xbd\x8d(\xe6\x97\xa5\xe6\x9c\x9f\xe5\x80\xbc)') |
| 8 | fvalue | b'float' | YES | bytearray(b'\xe9\xa2\x84\xe7\x95\x99\xe6\xa0\x87\xe5\xbf\x97\xe4\xbd\x8d(\xe6\xb5\xae\xe7\x82\xb9\xe5\x80\xbc)') |
| 1 | id | b'int(11)' | NO | bytearray(b'id') |
| 7 | ivalue | b'int(11)' | YES | bytearray(b'\xe9\xa2\x84\xe7\x95\x99\xe6\xa0\x87\xe5\xbf\x97\xe4\xbd\x8d(\xe6\x95\xb4\xe5\xbd\xa2\xe5\x80\xbc)') |
| 13 | jy_time | b'date' | YES | bytearray(b'\xe8\x81\x9a\xe6\xba\x90\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 11 | modified_time | b'datetime' | YES | bytearray(b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4') |



### s03_sy_jy_middle_tree () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | create_time | b'datetime' | NO | bytearray(b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4') |
| 1 | id | b'int(11)' | NO | bytearray(b'\xe8\x87\xaa\xe5\xa2\x9eID') |
| 3 | jy_node | b'int(11)' | NO | bytearray(b'\xe8\x81\x9a\xe6\xba\x90\xe4\xbb\xa3\xe7\xa0\x81') |
| 5 | modified_time | b'datetime' | NO | bytearray(b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4') |
| 4 | node_category | b'tinyint(3)' | NO | bytearray(b'1-\xe5\xad\x97\xe8\x8a\x82\xe7\x82\xb9\xef\xbc\x8c2-\xe5\x8f\xb6\xe8\x8a\x82\xe7\x82\xb9') |
| 2 | sy_node | b'bigint(20)' | NO | bytearray(b'\xe7\x86\xb5\xe4\xb8\x80\xe4\xbb\xa3\xe7\xa0\x81') |



### s04_c_ed_indicatortree () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | BrotherNo | b'int(11)' | YES | bytearray(b'\xe5\x90\x8c\xe4\xb8\x80\xe5\xb1\x82\xe7\xba\xa7\xe5\xba\x8f\xe5\x8f\xb7') |
| 5 | ChiSpelling | b'varchar(150)' | YES | bytearray(b'') |
| 1 | ID | b'bigint(20)' | NO | bytearray(b'ID') |
| 12 | JSID | b'bigint(20)' | NO | bytearray(b'JSID') |
| 8 | LevelNumber | b'tinyint(3)' | YES | bytearray(b'\xe5\xb1\x82\xe7\xba\xa7\xe6\xb7\xb1\xe5\xba\xa6') |
| 4 | NodeAbbr | b'varchar(300)' | YES | bytearray(b'') |
| 2 | NodeCode | b'int(11)' | NO | bytearray(b'\xe7\xbb\x93\xe7\x82\xb9\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | NodeName | b'varchar(300)' | NO | bytearray(b'\xe7\xbb\x93\xe7\x82\xb9\xe5\x90\x8d\xe7\xa7\xb0') |
| 10 | NodeState | b'tinyint(3)' | YES | bytearray(b'\xe7\xbb\x93\xe7\x82\xb9\xe7\x8a\xb6\xe6\x80\x81') |
| 9 | NoteCategory | b'tinyint(3)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe7\xb1\xbb\xe5\x9e\x8b') |
| 6 | ParentNode | b'int(11)' | YES | bytearray(b'\xe7\x88\xb6\xe8\x8a\x82\xe7\x82\xb9\xe4\xbb\xa3\xe7\xa0\x81') |
| 11 | UpdateTime | b'datetime' | NO | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s04_c_ged_indicatortree () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | BrotherNo | b'int(11)' | YES | bytearray(b'\xe5\x90\x8c\xe4\xb8\x80\xe5\xb1\x82\xe7\xba\xa7\xe5\xba\x8f\xe5\x8f\xb7') |
| 10 | CatalogStru | b'int(11)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe7\x9b\xae\xe5\xbd\x95\xe7\xbb\x93\xe6\x9e\x84') |
| 1 | ID | b'bigint(20)' | NO | bytearray(b'ID') |
| 13 | JSID | b'bigint(20)' | NO | bytearray(b'JSID') |
| 8 | LevelNumber | b'int(11)' | YES | bytearray(b'\xe5\xb1\x82\xe7\xba\xa7\xe6\xb7\xb1\xe5\xba\xa6') |
| 4 | NodeAbbrCH | b'varchar(300)' | YES | bytearray(b'') |
| 5 | NodeAbbrEN | b'varchar(300)' | YES | bytearray(b'') |
| 2 | NodeCode | b'bigint(20)' | NO | bytearray(b'\xe7\xbb\x93\xe7\x82\xb9\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | NodeName | b'varchar(300)' | YES | bytearray(b'\xe7\xbb\x93\xe7\x82\xb9\xe5\x90\x8d\xe7\xa7\xb0') |
| 11 | NodeState | b'tinyint(3)' | YES | bytearray(b'\xe7\xbb\x93\xe7\x82\xb9\xe7\x8a\xb6\xe6\x80\x81') |
| 9 | NoteCategory | b'tinyint(3)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe7\xb1\xbb\xe5\x9e\x8b') |
| 6 | ParentNode | b'bigint(20)' | YES | bytearray(b'\xe7\x88\xb6\xe8\x8a\x82\xe7\x82\xb9\xe4\xbb\xa3\xe7\xa0\x81') |
| 12 | UpdateTime | b'datetime' | NO | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s04_c_in_indicatortree () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | BrotherNo | b'int(11)' | YES | bytearray(b'\xe5\x90\x8c\xe4\xb8\x80\xe5\xb1\x82\xe7\xba\xa7\xe5\xba\x8f\xe5\x8f\xb7') |
| 5 | ChiSpelling | b'varchar(150)' | YES | bytearray(b'') |
| 1 | ID | b'bigint(20)' | YES | bytearray(b'ID') |
| 12 | JSID | b'bigint(20)' | YES | bytearray(b'JSID') |
| 8 | LevelNumber | b'tinyint(3)' | YES | bytearray(b'\xe5\xb1\x82\xe7\xba\xa7\xe6\xb7\xb1\xe5\xba\xa6') |
| 4 | NodeAbbr | b'varchar(300)' | YES | bytearray(b'') |
| 2 | NodeCode | b'int(11)' | YES | bytearray(b'\xe7\xbb\x93\xe7\x82\xb9\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | NodeName | b'varchar(300)' | YES | bytearray(b'\xe7\xbb\x93\xe7\x82\xb9\xe5\x90\x8d\xe7\xa7\xb0') |
| 10 | NodeState | b'tinyint(3)' | YES | bytearray(b'\xe7\xbb\x93\xe7\x82\xb9\xe7\x8a\xb6\xe6\x80\x81') |
| 9 | NoteCategory | b'tinyint(3)' | YES | bytearray(b'\xe8\x8a\x82\xe7\x82\xb9\xe7\xb1\xbb\xe5\x9e\x8b') |
| 6 | ParentNode | b'int(11)' | YES | bytearray(b'\xe7\x88\xb6\xe8\x8a\x82\xe7\x82\xb9\xe4\xbb\xa3\xe7\xa0\x81') |
| 11 | UpdateTime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s04_cn_eco_base () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | CNName | b'varchar(800)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d') |
| 1 | EndDate | b'datetime' | NO | bytearray(b'') |
| 3 | IndicatorCode | b'varchar(200)' | NO | bytearray(b'') |
| 2 | InfoPublDate | b'datetime' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f') |
| 6 | Measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe5\x8d\x95\xe4\xbd\x8d') |
| 8 | Organization | b'varchar(20)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe5\x8f\x91\xe5\xb8\x83\xe6\x9c\xba\xe6\x9e\x84') |
| 7 | Period | b'varchar(10)' | YES | bytearray(b'\xe9\xa2\x91\xe5\xba\xa6') |
| 9 | Source | b'varchar(50)' | YES | bytearray(b'\xe9\x8f\x81\xe7\x89\x88\xe5\xb5\x81\xe5\xa9\xa7\xe6\x84\xae\xe7\xb6\x89\xe9\x8d\xa7\xe2\x82\xac') |
| 10 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 5 | Value | b'decimal(28,6)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe5\x80\xbc') |



### s04_prod () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 8 | CValue | b'decimal(18,5)' | NO | bytearray(b'') |
| 10 | DailyReturn | b'decimal(18,6)' | YES | bytearray(b'') |
| 11 | Dropdown | b'decimal(18,6)' | YES | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 13 | IsDvdYear | b'int(11)' | YES | bytearray(b'') |
| 9 | MaxValue | b'decimal(18,5)' | NO | bytearray(b'') |
| 5 | ProdAUM | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | ProdID | b'varchar(20)' | NO | bytearray(b'') |
| 4 | ProdName | b'varchar(200)' | NO | bytearray(b'') |
| 6 | ProdShare | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | UpdateTime | b'datetime' | NO | bytearray(b'') |
| 2 | ValuationDate | b'datetime(6)' | NO | bytearray(b'') |
| 7 | Value | b'decimal(18,5)' | NO | bytearray(b'') |



### s04_report_base () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | cnname | b'varchar(800)' | NO | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d') |
| 10 | create_time | b'datetime' | YES | bytearray(b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4') |
| 1 | end_date | b'datetime' | NO | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f') |
| 3 | indicator_code | b'varchar(200)' | NO | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | info_publ_date | b'datetime' | YES | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe6\xba\x90\xe6\x97\xa5\xe6\x9c\x9f') |
| 6 | measurment | b'varchar(20)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe5\x8d\x95\xe4\xbd\x8d') |
| 11 | modified_time | b'datetime' | YES | bytearray(b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4') |
| 8 | organization | b'varchar(20)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe5\x8f\x91\xe5\xb8\x83\xe6\x9c\xba\xe6\x9e\x84') |
| 7 | period | b'varchar(10)' | YES | bytearray(b'\xe9\xa2\x91\xe5\xba\xa6') |
| 9 | source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\x9d\xa5\xe6\xba\x90') |
| 5 | value | b'decimal(28,6)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe5\x80\xbc') |



### s05_cn_stock_data () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | BillReceivable | b'decimal(25,4)' | YES | bytearray(b'\xe5\xba\x94\xe6\x94\xb6\xe7\xa5\xa8\xe6\x8d\xae') |
| 6 | CashEquivalents | b'decimal(25,4)' | YES | bytearray(b'\xe8\xb4\xa7\xe5\xb8\x81\xe8\xb5\x84\xe9\x87\x91') |
| 23 | Data | b'decimal(25,4)' | YES | bytearray(b'\xe8\x87\xaa\xe7\x94\xb1\xe7\x8e\xb0\xe9\x87\x91\xe6\xb5\x81\xe9\x87\x8f\xef\xbc\x88\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe5\xbc\x8f_\xe5\xbe\x85\xe8\x8e\xb7\xe5\xbe\x97\xef\xbc\x89') |
| 2 | Date | b'varchar(10)' | NO | bytearray(b'\xe6\x97\xa5\xe6\x9c\x9f') |
| 24 | Father_node | b'varchar(12)' | NO | bytearray(b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0') |
| 21 | FCFF | b'decimal(25,4)' | YES | bytearray(b'\xe4\xbc\x81\xe4\xb8\x9a\xe8\x87\xaa\xe7\x94\xb1\xe7\x8e\xb0\xe9\x87\x91\xe6\xb5\x81\xe9\x87\x8f\xef\xbc\x88FCFF\xef\xbc\x89') |
| 10 | FixIntanOtherAssetAcquiCash | b'decimal(25,4)' | YES | bytearray(b'\xe5\x8d\x95\xe5\xad\xa3\xe5\xba\xa6.\xe8\xb4\xad\xe5\xbb\xba\xe5\x9b\xba\xe5\xae\x9a\xe8\xb5\x84\xe4\xba\xa7\xe3\x80\x81\xe6\x97\xa0\xe5\xbd\xa2\xe8\xb5\x84\xe4\xba\xa7\xe5\x92\x8c\xe5\x85\xb6\xe4\xbb\x96\xe9\x95\xbf\xe6\x9c\x9f\xe8\xb5\x84\xe4\xba\xa7\xe6\x94\xaf\xe4\xbb\x98\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 20 | GrossProfitTTM | b'decimal(25,4)' | YES | bytearray(b'\xe6\xaf\x9b\xe5\x88\xa9\xef\xbc\x88TTM\xef\xbc\x89') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 19 | InterestBearDebt | b'decimal(25,4)' | YES | bytearray(b'\xe5\xb8\xa6\xe6\x81\xaf\xe5\x80\xba\xe5\x8a\xa1') |
| 8 | Inventories | b'decimal(25,4)' | YES | bytearray(b'\xe5\xad\x98\xe8\xb4\xa7') |
| 18 | NetOperateCashFlowTTM | b'decimal(25,4)' | YES | bytearray(b'\xe7\xbb\x8f\xe8\x90\xa5\xe6\xb4\xbb\xe5\x8a\xa8\xe7\x8e\xb0\xe9\x87\x91\xe5\x87\x80\xe6\xb5\x81\xe9\x87\x8f(TTM)') |
| 15 | NetProfitCut | b'decimal(25,4)' | YES | bytearray(b'\xe6\x89\xa3\xe9\x99\xa4\xe9\x9d\x9e\xe7\xbb\x8f\xe5\xb8\xb8\xe6\x80\xa7\xe6\x8d\x9f\xe7\x9b\x8a\xe5\x90\x8e\xe7\x9a\x84\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6\xef\xbc\x88\xe9\x9d\x9eTTM\xef\xbc\x89\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe5\xbc\x8f\xe5\xbe\x85\xe8\x8e\xb7\xe5\xbe\x97') |
| 12 | NPFromParentCompanyOwners | b'decimal(25,4)' | YES | bytearray(b'\xe5\x8d\x95\xe5\xad\xa3\xe5\xba\xa6.\xe5\xbd\x92\xe5\xb1\x9e\xe6\xaf\x8d\xe5\x85\xac\xe5\x8f\xb8\xe8\x82\xa1\xe4\xb8\x9c\xe7\x9a\x84\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6') |
| 17 | NPParentCompanyOwnersTTM | b'decimal(25,4)' | YES | bytearray(b'\xe5\xbd\x92\xe5\xb1\x9e\xe6\xaf\x8d\xe5\x85\xac\xe5\x8f\xb8\xe8\x82\xa1\xe4\xb8\x9c\xe7\x9a\x84\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6\xef\xbc\x88TTM\xef\xbc\x89') |
| 11 | OperatingRevenue | b'decimal(25,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5') |
| 16 | OperatingRevenueTTM | b'decimal(25,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5\xef\xbc\x88TTM\xef\xbc\x89') |
| 22 | qfa_grossmargin | b'decimal(25,4)' | YES | bytearray(b'\xe5\x8d\x95\xe5\xad\xa3\xe5\xba\xa6.\xe6\xaf\x9b\xe5\x88\xa9') |
| 13 | qfa_OperatingRevenue | b'decimal(25,4)' | YES | bytearray(b'\xe5\x8d\x95\xe5\xad\xa3\xe5\xba\xa6.\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5') |
| 9 | SEWithoutMI | b'decimal(25,4)' | YES | bytearray(b'\xe5\xbd\x92\xe5\xb1\x9e\xe6\xaf\x8d\xe5\x85\xac\xe5\x8f\xb8\xe8\x82\xa1\xe4\xb8\x9c\xe7\x9a\x84\xe6\x9d\x83\xe7\x9b\x8a') |
| 3 | Stock_ID | b'varchar(10)' | NO | bytearray(b'\xe8\x82\xa1\xe6\x8c\x87\xe5\x90\x8d\xe7\xa7\xb0') |
| 5 | TotalAssets | b'decimal(25,4)' | YES | bytearray(b'\xe8\xb5\x84\xe4\xba\xa7\xe6\x80\xbb\xe8\xae\xa1') |
| 4 | TotalLiability | b'decimal(25,4)' | YES | bytearray(b'\xe8\xb4\x9f\xe5\x80\xba\xe5\x90\x88\xe8\xae\xa1') |
| 14 | TotalMV | b'decimal(25,4)' | YES | bytearray(b'\xe6\x80\xbb\xe5\xb8\x82\xe5\x80\xbc2') |
| 25 | Update_time | b'varchar(20)' | NO | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s05_us_bls_consumer_data () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | InfoPublDate | b'datetime' | NO | bytearray(b'') |
| 8 | Organization | b'varchar(40)' | YES | bytearray(b'') |
| 6 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 4 | Period_BLS | b'varchar(10)' | YES | bytearray(b'') |
| 5 | Periodname_BLS | b'varchar(10)' | YES | bytearray(b'') |
| 2 | Series_ID | b'varchar(30)' | NO | bytearray(b'BLS\xe7\xbc\x96\xe7\xa0\x81') |
| 7 | Source | b'varchar(10)' | YES | bytearray(b'') |
| 9 | Updatetime | b'datetime' | YES | bytearray(b'') |
| 10 | Value | b'decimal(18,6)' | YES | bytearray(b'') |
| 3 | Year_BLS | b'varchar(10)' | YES | bytearray(b'') |



### s05_us_bls_consumer_data_ap () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | InfoPublDate | b'datetime' | NO | bytearray(b'') |
| 8 | Organization | b'varchar(40)' | YES | bytearray(b'') |
| 6 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 4 | Period_BLS | b'varchar(10)' | YES | bytearray(b'') |
| 5 | Periodname_BLS | b'varchar(10)' | YES | bytearray(b'') |
| 2 | Series_ID | b'varchar(30)' | NO | bytearray(b'') |
| 7 | Source | b'varchar(10)' | YES | bytearray(b'') |
| 9 | Updatetime | b'datetime' | YES | bytearray(b'') |
| 10 | Value | b'decimal(18,6)' | YES | bytearray(b'') |
| 3 | Year_BLS | b'varchar(10)' | YES | bytearray(b'') |



### s05_us_bls_consumer_data_cw () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | InfoPublDate | b'datetime' | NO | bytearray(b'') |
| 8 | Organization | b'varchar(40)' | YES | bytearray(b'') |
| 6 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 4 | Period_BLS | b'varchar(10)' | YES | bytearray(b'') |
| 5 | Periodname_BLS | b'varchar(10)' | YES | bytearray(b'') |
| 2 | Series_ID | b'varchar(30)' | NO | bytearray(b'') |
| 7 | Source | b'varchar(10)' | YES | bytearray(b'') |
| 9 | Updatetime | b'datetime' | YES | bytearray(b'') |
| 10 | Value | b'decimal(18,6)' | YES | bytearray(b'') |
| 3 | Year_BLS | b'varchar(10)' | YES | bytearray(b'') |



### s05_us_bls_consumer_data_ei () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 10 | DataValue | b'decimal(18,6)' | YES | bytearray(b'\xe5\x80\xbc') |
| 1 | InfoPublDate | b'datetime' | NO | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f') |
| 8 | Organization | b'varchar(40)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\x9d\xa5\xe6\xba\x90\xe7\xbb\x84\xe7\xbb\x87') |
| 6 | Period | b'varchar(10)' | YES | bytearray(b'\xe9\xa2\x91\xe7\x8e\x87') |
| 4 | Period_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80') |
| 5 | Periodname_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80\xe5\x91\xa8\xe6\x9c\x9f\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d') |
| 2 | Series_ID | b'varchar(30)' | NO | bytearray(b'\xe7\xb3\xbb\xe5\x88\x97ID') |
| 7 | Source | b'varchar(10)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe8\x8e\xb7\xe5\x8f\x96\xe6\x96\xb9\xe5\xbc\x8f') |
| 9 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4') |
| 3 | Year_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80\xe5\xb9\xb4\xe4\xbb\xbd') |



### s05_us_bls_consumer_data_pc () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 10 | DataValue | b'decimal(18,6)' | YES | bytearray(b'\xe5\x80\xbc') |
| 1 | InfoPublDate | b'datetime' | NO | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f') |
| 8 | Organization | b'varchar(40)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\x9d\xa5\xe6\xba\x90\xe7\xbb\x84\xe7\xbb\x87') |
| 6 | Period | b'varchar(10)' | YES | bytearray(b'\xe9\xa2\x91\xe7\x8e\x87') |
| 4 | Period_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80') |
| 5 | Periodname_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80\xe5\x91\xa8\xe6\x9c\x9f\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d') |
| 2 | Series_ID | b'varchar(30)' | NO | bytearray(b'\xe7\xb3\xbb\xe5\x88\x97ID') |
| 7 | Source | b'varchar(10)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe8\x8e\xb7\xe5\x8f\x96\xe6\x96\xb9\xe5\xbc\x8f') |
| 9 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4') |
| 3 | Year_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80\xe5\xb9\xb4\xe4\xbb\xbd') |



### s05_us_bls_consumer_data_su () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | InfoPublDate | b'datetime' | NO | bytearray(b'') |
| 8 | Organization | b'varchar(40)' | YES | bytearray(b'') |
| 6 | Period | b'varchar(10)' | YES | bytearray(b'') |
| 4 | Period_BLS | b'varchar(10)' | YES | bytearray(b'') |
| 5 | Periodname_BLS | b'varchar(10)' | YES | bytearray(b'') |
| 2 | Series_ID | b'varchar(30)' | NO | bytearray(b'') |
| 7 | Source | b'varchar(10)' | YES | bytearray(b'') |
| 9 | Updatetime | b'datetime' | YES | bytearray(b'') |
| 10 | Value | b'decimal(18,6)' | YES | bytearray(b'') |
| 3 | Year_BLS | b'varchar(10)' | YES | bytearray(b'') |



### s05_us_bls_consumer_data_wp () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 10 | DataValue | b'decimal(18,6)' | YES | bytearray(b'\xe5\x80\xbc') |
| 1 | InfoPublDate | b'datetime' | NO | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f') |
| 8 | Organization | b'varchar(40)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\x9d\xa5\xe6\xba\x90\xe7\xbb\x84\xe7\xbb\x87') |
| 6 | Period | b'varchar(10)' | YES | bytearray(b'\xe9\xa2\x91\xe7\x8e\x87') |
| 4 | Period_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80') |
| 5 | Periodname_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80\xe5\x91\xa8\xe6\x9c\x9f\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d') |
| 2 | Series_ID | b'varchar(30)' | NO | bytearray(b'\xe7\xb3\xbb\xe5\x88\x97ID') |
| 7 | Source | b'varchar(10)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe8\x8e\xb7\xe5\x8f\x96\xe6\x96\xb9\xe5\xbc\x8f') |
| 9 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4') |
| 3 | Year_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80\xe5\xb9\xb4\xe4\xbb\xbd') |



### s05_us_bls_consumer_mapping () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | AreaCode | b'varchar(10)' | YES | bytearray(b'') |
| 6 | BaseCode | b'varchar(5)' | YES | bytearray(b'') |
| 7 | BasePeriod | b'varchar(30)' | YES | bytearray(b'') |
| 11 | BeginPeriod | b'varchar(10)' | YES | bytearray(b'') |
| 10 | BeginYear | b'varchar(10)' | YES | bytearray(b'') |
| 13 | EndPeriod | b'varchar(10)' | YES | bytearray(b'') |
| 12 | EndYear | b'varchar(10)' | YES | bytearray(b'') |
| 9 | FootnoteCodes | b'varchar(30)' | YES | bytearray(b'') |
| 3 | ItemCode | b'varchar(10)' | YES | bytearray(b'') |
| 5 | PeriodicityCode | b'varchar(5)' | YES | bytearray(b'') |
| 4 | Seasonal | b'varchar(5)' | YES | bytearray(b'') |
| 1 | Series_ID | b'varchar(30)' | NO | bytearray(b'BLS\xe7\xbc\x96\xe7\xa0\x81') |
| 8 | SeriesTitle | b'varchar(200)' | YES | bytearray(b'') |



### s05_us_bls_consumer_mapping_ap () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | AreaCode | b'varchar(10)' | YES | bytearray(b'') |
| 7 | BeginPeriod | b'varchar(10)' | YES | bytearray(b'') |
| 6 | BeginYear | b'varchar(10)' | YES | bytearray(b'') |
| 9 | EndPeriod | b'varchar(10)' | YES | bytearray(b'') |
| 8 | EndYear | b'varchar(10)' | YES | bytearray(b'') |
| 5 | FootnoteCodes | b'varchar(30)' | YES | bytearray(b'') |
| 3 | ItemCode | b'varchar(10)' | YES | bytearray(b'') |
| 1 | Series_ID | b'varchar(30)' | NO | bytearray(b'') |
| 4 | SeriesTitle | b'varchar(200)' | YES | bytearray(b'') |



### s05_us_bls_consumer_mapping_cw () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | AreaCode | b'varchar(10)' | YES | bytearray(b'') |
| 6 | BaseCode | b'varchar(5)' | YES | bytearray(b'') |
| 7 | BasePeriod | b'varchar(30)' | YES | bytearray(b'') |
| 11 | BeginPeriod | b'varchar(10)' | YES | bytearray(b'') |
| 10 | BeginYear | b'varchar(10)' | YES | bytearray(b'') |
| 13 | EndPeriod | b'varchar(10)' | YES | bytearray(b'') |
| 12 | EndYear | b'varchar(10)' | YES | bytearray(b'') |
| 9 | FootnoteCodes | b'varchar(30)' | YES | bytearray(b'') |
| 3 | ItemCode | b'varchar(10)' | YES | bytearray(b'') |
| 5 | PeriodicityCode | b'varchar(5)' | YES | bytearray(b'') |
| 4 | Seasonal | b'varchar(5)' | YES | bytearray(b'') |
| 1 | Series_ID | b'varchar(30)' | NO | bytearray(b'') |
| 8 | SeriesTitle | b'varchar(200)' | YES | bytearray(b'') |



### s05_us_bls_consumer_mapping_ei () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | BaseDate | b'varchar(30)' | YES | bytearray(b'\xe5\x9f\xba\xe5\x87\x86\xe6\x97\xa5\xe6\x9c\x9f') |
| 9 | BeginPeriod | b'varchar(10)' | YES | bytearray(b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe6\x9c\x9f') |
| 8 | BeginYear | b'varchar(10)' | YES | bytearray(b'\xe8\xb5\xb7\xe5\xa7\x8b\xe5\xb9\xb4\xe4\xbb\xbd') |
| 11 | EndPeriod | b'varchar(10)' | YES | bytearray(b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe6\x9c\x9f') |
| 10 | EndYear | b'varchar(10)' | YES | bytearray(b'\xe7\xbb\x93\xe6\x9d\x9f\xe5\xb9\xb4\xe4\xbb\xbd') |
| 7 | FootnoteCodes | b'varchar(30)' | YES | bytearray(b'\xe8\x84\x9a\xe6\xb3\xa8') |
| 3 | IndexCode | b'varchar(30)' | YES | bytearray(b'\xe7\xb4\xa2\xe5\xbc\x95\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | Seasonal | b'varchar(5)' | YES | bytearray(b'\xe6\x97\xb6\xe4\xbb\xa4') |
| 1 | Series_ID | b'varchar(30)' | NO | bytearray(b'\xe7\xb3\xbb\xe5\x88\x97ID') |
| 4 | SeriesName | b'varchar(300)' | YES | bytearray(b'\xe7\xb3\xbb\xe5\x88\x97\xe5\x90\x8d') |
| 6 | SeriesTitle | b'varchar(300)' | YES | bytearray(b'\xe7\xb3\xbb\xe5\x88\x97\xe6\xa0\x87\xe9\xa2\x98') |



### s05_us_bls_consumer_mapping_pc () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | BaseDate | b'varchar(30)' | YES | bytearray(b'\xe5\x9f\xba\xe5\x87\x86\xe6\x97\xa5\xe6\x9c\x9f') |
| 9 | BeginPeriod | b'varchar(10)' | YES | bytearray(b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe6\x9c\x9f') |
| 8 | BeginYear | b'varchar(10)' | YES | bytearray(b'\xe8\xb5\xb7\xe5\xa7\x8b\xe5\xb9\xb4\xe4\xbb\xbd') |
| 11 | EndPeriod | b'varchar(10)' | YES | bytearray(b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe6\x9c\x9f') |
| 10 | EndYear | b'varchar(10)' | YES | bytearray(b'\xe7\xbb\x93\xe6\x9d\x9f\xe5\xb9\xb4\xe4\xbb\xbd') |
| 7 | FootnoteCodes | b'varchar(30)' | YES | bytearray(b'\xe8\x84\x9a\xe6\xb3\xa8') |
| 2 | IndustryCode | b'varchar(30)' | YES | bytearray(b'\xe8\xa1\x8c\xe4\xb8\x9a\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | ProductCode | b'varchar(30)' | YES | bytearray(b'\xe4\xba\xa7\xe5\x93\x81\xe4\xbb\xa3\xe7\xa0\x81') |
| 4 | Seasonal | b'varchar(5)' | YES | bytearray(b'\xe6\x97\xb6\xe4\xbb\xa4') |
| 1 | Series_ID | b'varchar(30)' | NO | bytearray(b'\xe7\xb3\xbb\xe5\x88\x97ID') |
| 6 | SeriesTitle | b'varchar(200)' | YES | bytearray(b'\xe7\xb3\xbb\xe5\x88\x97\xe6\xa0\x87\xe9\xa2\x98') |



### s05_us_bls_consumer_mapping_su () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | AreaCode | b'varchar(10)' | YES | bytearray(b'') |
| 6 | BaseCode | b'varchar(5)' | YES | bytearray(b'') |
| 7 | BasePeriod | b'varchar(30)' | YES | bytearray(b'') |
| 11 | BeginPeriod | b'varchar(10)' | YES | bytearray(b'') |
| 10 | BeginYear | b'varchar(10)' | YES | bytearray(b'') |
| 13 | EndPeriod | b'varchar(10)' | YES | bytearray(b'') |
| 12 | EndYear | b'varchar(10)' | YES | bytearray(b'') |
| 9 | FootnoteCodes | b'varchar(30)' | YES | bytearray(b'') |
| 3 | ItemCode | b'varchar(10)' | YES | bytearray(b'') |
| 5 | PeriodicityCode | b'varchar(5)' | YES | bytearray(b'') |
| 4 | Seasonal | b'varchar(5)' | YES | bytearray(b'') |
| 1 | Series_ID | b'varchar(30)' | NO | bytearray(b'') |
| 8 | SeriesTitle | b'varchar(200)' | YES | bytearray(b'') |



### s05_us_bls_consumer_mapping_wp () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | BaseDate | b'varchar(30)' | YES | bytearray(b'\xe5\x9f\xba\xe5\x87\x86\xe6\x97\xa5\xe6\x9c\x9f') |
| 9 | BeginPeriod | b'varchar(10)' | YES | bytearray(b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe6\x9c\x9f') |
| 8 | BeginYear | b'varchar(10)' | YES | bytearray(b'\xe8\xb5\xb7\xe5\xa7\x8b\xe5\xb9\xb4\xe4\xbb\xbd') |
| 11 | EndPeriod | b'varchar(10)' | YES | bytearray(b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe6\x9c\x9f') |
| 10 | EndYear | b'varchar(10)' | YES | bytearray(b'\xe7\xbb\x93\xe6\x9d\x9f\xe5\xb9\xb4\xe4\xbb\xbd') |
| 7 | FootnoteCodes | b'varchar(30)' | YES | bytearray(b'\xe8\x84\x9a\xe6\xb3\xa8') |
| 2 | GroupCode | b'varchar(30)' | YES | bytearray(b'\xe7\xbb\x84\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | ItemCode | b'varchar(30)' | YES | bytearray(b'\xe9\xa1\xb9\xe7\x9b\xae\xe4\xbb\xa3\xe7\xa0\x81') |
| 4 | Seasonal | b'varchar(5)' | YES | bytearray(b'\xe6\x97\xb6\xe4\xbb\xa4') |
| 1 | Series_ID | b'varchar(30)' | NO | bytearray(b'\xe7\xb3\xbb\xe5\x88\x97ID') |
| 6 | SeriesTitle | b'varchar(300)' | YES | bytearray(b'\xe7\xb3\xbb\xe5\x88\x97\xe6\xa0\x87\xe9\xa2\x98') |



### s05_us_bls_enployment_monthly_data_ce () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 10 | DataValue | b'decimal(18,6)' | YES | bytearray(b'\xe5\x80\xbc') |
| 1 | InfoPublDate | b'datetime' | NO | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f') |
| 8 | Organization | b'varchar(40)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\x9d\xa5\xe6\xba\x90\xe7\xbb\x84\xe7\xbb\x87') |
| 6 | Period | b'varchar(10)' | YES | bytearray(b'\xe9\xa2\x91\xe7\x8e\x87') |
| 4 | Period_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80') |
| 5 | Periodname_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80\xe5\x91\xa8\xe6\x9c\x9f\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d') |
| 2 | Series_ID | b'varchar(30)' | NO | bytearray(b'\xe7\xb3\xbb\xe5\x88\x97ID') |
| 7 | Source | b'varchar(10)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe8\x8e\xb7\xe5\x8f\x96\xe6\x96\xb9\xe5\xbc\x8f') |
| 9 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4') |
| 3 | Year_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80\xe5\xb9\xb4\xe4\xbb\xbd') |



### s05_us_bls_enployment_monthly_data_in () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 10 | DataValue | b'decimal(18,6)' | YES | bytearray(b'\xe5\x80\xbc') |
| 1 | InfoPublDate | b'datetime' | NO | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f') |
| 8 | Organization | b'varchar(40)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\x9d\xa5\xe6\xba\x90\xe7\xbb\x84\xe7\xbb\x87') |
| 6 | Period | b'varchar(10)' | YES | bytearray(b'\xe9\xa2\x91\xe7\x8e\x87') |
| 4 | Period_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80') |
| 5 | Periodname_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80\xe5\x91\xa8\xe6\x9c\x9f\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d') |
| 2 | Series_ID | b'varchar(30)' | NO | bytearray(b'\xe7\xb3\xbb\xe5\x88\x97ID') |
| 7 | Source | b'varchar(10)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe8\x8e\xb7\xe5\x8f\x96\xe6\x96\xb9\xe5\xbc\x8f') |
| 9 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4') |
| 3 | Year_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80\xe5\xb9\xb4\xe4\xbb\xbd') |



### s05_us_bls_enployment_monthly_data_jt () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 10 | DataValue | b'decimal(18,6)' | YES | bytearray(b'\xe5\x80\xbc') |
| 1 | InfoPublDate | b'datetime' | NO | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f') |
| 8 | Organization | b'varchar(40)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\x9d\xa5\xe6\xba\x90\xe7\xbb\x84\xe7\xbb\x87') |
| 6 | Period | b'varchar(10)' | YES | bytearray(b'\xe9\xa2\x91\xe7\x8e\x87') |
| 4 | Period_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80') |
| 5 | Periodname_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80\xe5\x91\xa8\xe6\x9c\x9f\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d') |
| 2 | Series_ID | b'varchar(30)' | NO | bytearray(b'\xe7\xb3\xbb\xe5\x88\x97ID') |
| 7 | Source | b'varchar(10)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe8\x8e\xb7\xe5\x8f\x96\xe6\x96\xb9\xe5\xbc\x8f') |
| 9 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4') |
| 3 | Year_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80\xe5\xb9\xb4\xe4\xbb\xbd') |



### s05_us_bls_enployment_monthly_data_sm () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 10 | DataValue | b'decimal(18,6)' | YES | bytearray(b'\xe5\x80\xbc') |
| 1 | InfoPublDate | b'datetime' | NO | bytearray(b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f') |
| 8 | Organization | b'varchar(40)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\x9d\xa5\xe6\xba\x90\xe7\xbb\x84\xe7\xbb\x87') |
| 6 | Period | b'varchar(10)' | YES | bytearray(b'\xe9\xa2\x91\xe7\x8e\x87') |
| 4 | Period_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80') |
| 5 | Periodname_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80\xe5\x91\xa8\xe6\x9c\x9f\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d') |
| 2 | Series_ID | b'varchar(30)' | NO | bytearray(b'\xe7\xb3\xbb\xe5\x88\x97ID') |
| 7 | Source | b'varchar(10)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe8\x8e\xb7\xe5\x8f\x96\xe6\x96\xb9\xe5\xbc\x8f') |
| 9 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4') |
| 3 | Year_BLS | b'varchar(10)' | YES | bytearray(b'\xe5\x8a\xb3\xe5\xb7\xa5\xe7\xbb\x9f\xe8\xae\xa1\xe5\xb1\x80\xe5\xb9\xb4\xe4\xbb\xbd') |



### s05_us_bls_enployment_monthly_mapping_ce () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 9 | BeginPeriod | b'varchar(10)' | YES | bytearray(b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe6\x9c\x9f') |
| 8 | BeginYear | b'varchar(10)' | YES | bytearray(b'\xe8\xb5\xb7\xe5\xa7\x8b\xe5\xb9\xb4\xe4\xbb\xbd') |
| 4 | DataTypeCode | b'varchar(30)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe7\xb1\xbb\xe5\x9e\x8b\xe4\xbb\xa3\xe7\xa0\x81') |
| 11 | EndPeriod | b'varchar(10)' | YES | bytearray(b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe6\x9c\x9f') |
| 10 | EndYear | b'varchar(10)' | YES | bytearray(b'\xe7\xbb\x93\xe6\x9d\x9f\xe5\xb9\xb4\xe4\xbb\xbd') |
| 7 | FootnoteCodes | b'varchar(30)' | YES | bytearray(b'\xe8\x84\x9a\xe6\xb3\xa8') |
| 3 | IndustryCode | b'varchar(30)' | YES | bytearray(b'\xe8\xa1\x8c\xe4\xb8\x9a\xe4\xbb\xa3\xe7\xa0\x81') |
| 5 | Seasonal | b'varchar(5)' | YES | bytearray(b'\xe6\x97\xb6\xe4\xbb\xa4') |
| 1 | Series_ID | b'varchar(30)' | NO | bytearray(b'\xe7\xb3\xbb\xe5\x88\x97ID') |
| 6 | SeriesTitle | b'varchar(300)' | YES | bytearray(b'\xe7\xb3\xbb\xe5\x88\x97\xe6\xa0\x87\xe9\xa2\x98') |
| 2 | SupersectorCode | b'varchar(10)' | YES | bytearray(b'\xe8\xb6\x85\xe7\xba\xa7\xe9\x83\xa8\xe9\x97\xa8\xe6\x8c\x87\xe6\xa0\x87') |



### s05_us_bls_enployment_monthly_mapping_in () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | absn_code | b'varchar(30)' | YES | bytearray(b'\xe7\xbc\xba\xe5\xb8\xad\xef\xbc\x88\xe6\x99\xae\xe9\x81\x8d\xef\xbc\x8c\xe6\x98\xaf\xe5\x90\xa6\xe6\x94\xb6\xe8\xb4\xb9\xef\xbc\x89') |
| 6 | activity_code | b'varchar(30)' | YES | bytearray(b'\xe6\x95\x99\xe8\x82\xb2\xe9\x98\xb6\xe6\xae\xb5') |
| 7 | ages_code | b'varchar(10)' | YES | bytearray(b'\xe4\xb8\x8d\xe5\x90\x8c\xe5\xb9\xb4\xe9\xbe\x84\xe9\x98\xb6\xe6\xae\xb5') |
| 39 | begin_period | b'varchar(10)' | YES | bytearray(b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe6\x9c\x9f') |
| 38 | begin_year | b'varchar(10)' | YES | bytearray(b'\xe8\xb5\xb7\xe5\xa7\x8b\xe5\xb9\xb4\xe4\xbb\xbd') |
| 33 | born_code | b'varchar(10)' | YES | bytearray(b'\xe5\x87\xba\xe7\x94\x9f\xe5\xb9\xb4\xe6\x9c\x88') |
| 8 | cert_code | b'varchar(30)' | YES | bytearray(b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x9c\x89\xe8\xaf\x81\xe6\x98\x8e\xe5\x92\x8c\xe8\xae\xb8\xe5\x8f\xaf') |
| 34 | chld_code | b'varchar(10)' | YES | bytearray(b'\xe8\x87\xaa\xe5\xb7\xb1\xe6\x8a\x9a\xe5\x85\xbb\xe7\x9a\x84\xe5\xb0\x8f\xe5\xad\xa9\xef\xbc\x88\xe6\x8c\x89\xe6\x9c\x89\xe6\x97\xa0\xe5\x92\x8c\xe5\xb0\x8f\xe5\xad\xa9\xe5\xb9\xb4\xe9\xbe\x84\xe5\x8c\xba\xe5\x88\x86\xef\xbc\x89') |
| 9 | class_code | b'varchar(30)' | YES | bytearray(b'\xe5\x88\x86\xe7\xb1\xbb') |
| 35 | disa_code | b'varchar(10)' | YES | bytearray(b'\xe6\x98\xaf\xe5\x90\xa6\xe6\xae\x8b\xe7\x96\xbe') |
| 10 | duration_code | b'varchar(10)' | YES | bytearray(b'\xe6\x8c\x81\xe7\xbb\xad\xe5\x91\xa8\xe6\x95\xb0') |
| 11 | education_code | b'varchar(10)' | YES | bytearray(b'\xe5\x8f\x97\xe6\x95\x99\xe8\x82\xb2\xe7\xa8\x8b\xe5\xba\xa6') |
| 41 | end_period | b'varchar(10)' | YES | bytearray(b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe6\x9c\x9f') |
| 40 | end_year | b'varchar(10)' | YES | bytearray(b'\xe7\xbb\x93\xe6\x9d\x9f\xe5\xb9\xb4\xe4\xbb\xbd') |
| 12 | entr_code | b'varchar(10)' | YES | bytearray(b'\xe9\x87\x8d\xe6\x96\xb0\xe8\xbf\x9b\xe5\x85\xa5\xe5\x92\x8c\xe6\x96\xb0\xe8\xbf\x9b') |
| 13 | expr_code | b'varchar(10)' | YES | bytearray(b'\xe6\x9c\x89\xe6\x97\xa0\xe5\xb7\xa5\xe4\xbd\x9c\xe7\xbb\x8f\xe9\xaa\x8c') |
| 37 | footnote_codes | b'varchar(30)' | YES | bytearray(b'\xe8\x84\x9a\xe6\xb3\xa8') |
| 14 | hheader_code | b'varchar(10)' | YES | bytearray(b'\xe5\xae\xb6\xe5\xba\xad\xe4\xb8\xbb\xe7\xae\xa1') |
| 15 | hour_code | b'varchar(10)' | YES | bytearray(b'\xe6\x80\xbb\xe8\xae\xa1\xe5\xb0\x8f\xe6\x97\xb6') |
| 16 | indy_code | b'varchar(10)' | YES | bytearray(b'\xe4\xb8\x8d\xe5\x90\x8c\xe8\xa1\x8c\xe4\xb8\x9a') |
| 17 | jdes_code | b'varchar(10)' | YES | bytearray(b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x83\xb3\xe8\xa6\x81\xe4\xb8\x80\xe4\xb8\xaa\xe5\xb7\xa5\xe4\xbd\x9c') |
| 2 | lfst_code | b'varchar(30)' | YES | bytearray(b'\xe4\xb8\x8d\xe5\x90\x8c\xe5\xb7\xa5\xe4\xbd\x9c\xe7\x8a\xb6\xe6\x80\x81\xef\xbc\x88\xe5\x85\xa8\xe8\x81\x8c\xef\xbc\x8c\xe5\x85\xbc\xe8\x81\x8c\xef\xbc\x8c\xe6\x9c\xba\xe6\x9e\x84\xef\xbc\x8c\xe5\xa4\xb1\xe4\xb8\x9a\xe7\xad\x89\xe7\xad\x89\xef\xbc\x89') |
| 18 | look_code | b'varchar(10)' | YES | bytearray(b'\xe5\xb7\xa5\xe4\xbd\x9c\xe7\x9a\x84\xe7\x8a\xb6\xe6\x80\x81\xef\xbc\x88\xe5\xa4\xb1\xe4\xb8\x9a\xef\xbc\x8c\xe4\xb8\xb4\xe6\x97\xb6\xe9\x9b\x87\xe4\xbd\xa3\xef\xbc\x8c\xe8\xbe\x9e\xe8\x81\x8c\xef\xbc\x8c\xe9\x80\x80\xe4\xbc\x91\xef\xbc\x8c\xe5\xad\xa3\xe8\x8a\x82\xe5\xb7\xa5\xe7\xad\x89\xe7\xad\x89\xef\xbc\x89') |
| 19 | mari_code | b'varchar(10)' | YES | bytearray(b'\xe5\xa9\x9a\xe5\xa7\xbb\xe7\x8a\xb6\xe5\x86\xb5') |
| 20 | mjhs_code | b'varchar(10)' | YES | bytearray(b'\xe5\xa4\x9a\xe4\xb8\xaa\xe8\x81\x8c\xe4\xbd\x8d\xef\xbc\x88\xe4\xb8\xbb\xe8\xa6\x81\xe5\xb7\xa5\xe4\xbd\x9c\xe5\x92\x8c\xe5\x85\xb6\xe4\xbb\x96\xe5\xb7\xa5\xe4\xbd\x9c\xe6\x98\xaf\xe5\x85\xa8\xe8\x81\x8c\xef\xbc\x8c\xe5\x85\xbc\xe8\x81\x8c\xef\xbc\x8c\xe4\xb8\xb4\xe6\x97\xb6\xe7\xad\x89\xef\xbc\x89') |
| 21 | occupation_code | b'varchar(10)' | YES | bytearray(b'\xe4\xb8\x8d\xe5\x90\x8c\xe5\xb2\x97\xe4\xbd\x8d') |
| 22 | orig_code | b'varchar(10)' | YES | bytearray(b'\xe6\x89\x80\xe5\xb1\x9e\xe7\xa7\x8d\xe6\x97\x8f\xef\xbc\x88\xe5\x9b\xbd\xe5\xae\xb6\xef\xbc\x89') |
| 23 | pcts_code | b'varchar(10)' | YES | bytearray(b'\xe4\xb8\x8d\xe5\x90\x8c\xe5\xb7\xa5\xe4\xbd\x9c\xe7\x8a\xb6\xe6\x80\x81\xe6\x89\x80\xe5\x8d\xa0\xe7\x99\xbe\xe5\x88\x86\xe6\xaf\x94') |
| 3 | periodicity_code | b'varchar(30)' | YES | bytearray(b'\xe5\x91\xa8\xe6\x9c\x9f\xe6\x80\xa7\xe4\xbb\xa3\xe7\xa0\x81') |
| 24 | race_code | b'varchar(10)' | YES | bytearray(b'\xe5\x9b\xbd\xe5\xae\xb6\xe6\x88\x96\xe8\x82\xa4\xe8\x89\xb2') |
| 25 | rjnw_code | b'varchar(10)' | YES | bytearray(b'\xe6\xb2\xa1\xe5\x9c\xa8\xe5\xb7\xa5\xe4\xbd\x9c\xe7\x9a\x84\xe5\x8e\x9f\xe5\x9b\xa0') |
| 26 | rnlf_code | b'varchar(10)' | YES | bytearray(b'\xe5\xa4\xb1\xe4\xb8\x9a\xe7\x9b\xae\xe5\x89\x8d\xe7\x9a\x84\xe4\xb8\x80\xe4\xb8\xaa\xe7\x8a\xb6\xe6\x80\x81') |
| 27 | rwns_code | b'varchar(10)' | YES | bytearray(b'\xe5\x8e\x9f\xe5\x9b\xa0') |
| 36 | seasonal | b'varchar(10)' | YES | bytearray(b'\xe6\x98\xaf\xe5\x90\xa6\xe5\xad\xa3\xe8\x8a\x82\xe6\x80\xa7\xe8\xb0\x83\xe6\x95\xb4') |
| 28 | seek_code | b'varchar(10)' | YES | bytearray(b'\xe6\xad\xa3\xe5\x9c\xa8\xe6\x89\xbe\xe5\xb7\xa5\xe4\xbd\x9c') |
| 1 | series_id | b'varchar(30)' | NO | bytearray(b'\xe7\xb3\xbb\xe5\x88\x97ID') |
| 4 | series_title | b'varchar(10)' | YES | bytearray(b'\xe7\xb3\xbb\xe5\x88\x97\xe6\xa0\x87\xe9\xa2\x98') |
| 29 | sexs_code | b'varchar(10)' | YES | bytearray(b'\xe6\x80\xa7\xe5\x88\xab') |
| 30 | tdat_code | b'varchar(10)' | YES | bytearray(b'\xe5\xb7\xa5\xe4\xbd\x9c\xe6\x80\xbb\xe6\x97\xb6\xe9\x97\xb4') |
| 31 | vets_code | b'varchar(10)' | YES | bytearray(b'\xe4\xb8\xba\xe6\x88\x98\xe4\xba\x89\xe6\x9c\x8d\xe5\xbd\xb9\xef\xbc\x88\xe4\xba\x8c\xe6\x88\x98\xef\xbc\x8c\xe6\xb5\xb7\xe6\xb9\xbe\xef\xbc\x8c\xe8\xb6\x8a\xe5\x8d\x97\xe7\xad\x89\xe7\xad\x89\xef\xbc\x89') |
| 32 | wkst_code | b'varchar(10)' | YES | bytearray(b'\xe5\xb7\xa5\xe4\xbd\x9c\xe6\x97\xb6\xe9\x97\xb4') |



### s05_us_bls_enployment_monthly_mapping_jt () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 9 | begin_period | b'varchar(10)' | YES | bytearray(b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe6\x9c\x9f') |
| 8 | begin_year | b'varchar(10)' | YES | bytearray(b'\xe8\xb5\xb7\xe5\xa7\x8b\xe5\xb9\xb4\xe4\xbb\xbd') |
| 5 | dataelement_code | b'varchar(30)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe5\x85\x83\xe7\xb4\xa0\xe4\xbb\xa3\xe7\xa0\x81') |
| 11 | end_period | b'varchar(10)' | YES | bytearray(b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe6\x9c\x9f') |
| 10 | end_year | b'varchar(10)' | YES | bytearray(b'\xe7\xbb\x93\xe6\x9d\x9f\xe5\xb9\xb4\xe4\xbb\xbd') |
| 7 | footnote_codes | b'varchar(30)' | YES | bytearray(b'\xe8\x84\x9a\xe6\xb3\xa8') |
| 3 | industry_code | b'varchar(30)' | YES | bytearray(b'\xe8\xa1\x8c\xe4\xb8\x9a\xe4\xbb\xa3\xe7\xa0\x81') |
| 6 | ratelevel_code | b'varchar(300)' | YES | bytearray(b'\xe8\xb4\xb9\xe7\x8e\x87\xe6\xb0\xb4\xe5\xb9\xb3\xe4\xbb\xa3\xe7\xa0\x81') |
| 4 | region_code | b'varchar(5)' | YES | bytearray(b'\xe5\x8c\xba\xe5\x9f\x9f\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | seasonal | b'varchar(30)' | YES | bytearray(b'\xe6\x98\xaf\xe5\x90\xa6\xe5\xad\xa3\xe8\x8a\x82\xe6\x80\xa7\xe8\xb0\x83\xe6\x95\xb4') |
| 1 | series_id | b'varchar(30)' | NO | bytearray(b'\xe7\xb3\xbb\xe5\x88\x97ID') |



### s05_us_bls_enployment_monthly_mapping_sm () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | Area_Code | b'varchar(30)' | YES | bytearray(b'\xe5\x8c\xba\xe5\x9f\x9f\xe4\xbb\xa3\xe7\xa0\x81') |
| 11 | BeginPeriod | b'varchar(10)' | YES | bytearray(b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe6\x9c\x9f') |
| 10 | BeginYear | b'varchar(10)' | YES | bytearray(b'\xe8\xb5\xb7\xe5\xa7\x8b\xe5\xb9\xb4\xe4\xbb\xbd') |
| 8 | benchmark_year | b'varchar(30)' | YES | bytearray(b'\xe5\x9f\xba\xe5\x87\x86\xe5\xb9\xb4\xe4\xbb\xbd') |
| 6 | DataTypeCode | b'varchar(30)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe7\xb1\xbb\xe5\x9e\x8b\xe4\xbb\xa3\xe7\xa0\x81') |
| 13 | EndPeriod | b'varchar(10)' | YES | bytearray(b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe6\x9c\x9f') |
| 12 | EndYear | b'varchar(10)' | YES | bytearray(b'\xe7\xbb\x93\xe6\x9d\x9f\xe5\xb9\xb4\xe4\xbb\xbd') |
| 9 | FootnoteCodes | b'varchar(30)' | YES | bytearray(b'\xe8\x84\x9a\xe6\xb3\xa8') |
| 5 | IndustryCode | b'varchar(30)' | YES | bytearray(b'\xe8\xa1\x8c\xe4\xb8\x9a\xe4\xbb\xa3\xe7\xa0\x81') |
| 7 | Seasonal | b'varchar(5)' | YES | bytearray(b'\xe6\x97\xb6\xe4\xbb\xa4') |
| 1 | Series_ID | b'varchar(30)' | NO | bytearray(b'\xe7\xb3\xbb\xe5\x88\x97ID') |
| 2 | State_Code | b'varchar(30)' | YES | bytearray(b'\xe5\xb7\x9e\xe4\xbb\xa3\xe7\xa0\x81') |
| 4 | SupersectorCode | b'varchar(10)' | YES | bytearray(b'\xe8\xb6\x85\xe7\xba\xa7\xe9\x83\xa8\xe9\x97\xa8\xe6\x8c\x87\xe6\xa0\x87') |



### s05_us_stock_data () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 24 | BS_INVENTORIES | b'decimal(25,6)' | YES | bytearray(b'') |
| 14 | BS_TOT_ASSET | b'decimal(25,6)' | YES | bytearray(b'') |
| 19 | BS_TOT_LIAB2 | b'decimal(25,6)' | YES | bytearray(b'') |
| 21 | CAPITAL_EXPEND | b'decimal(25,6)' | YES | bytearray(b'') |
| 22 | CF_CASH_FROM_OPER | b'decimal(25,6)' | YES | bytearray(b'') |
| 28 | CF_FREE_CASH_FLOW | b'decimal(25,6)' | YES | bytearray(b'') |
| 4 | Chi_Name | b'varchar(35)' | YES | bytearray(b'') |
| 20 | CWithCE_AND_STI_DETAILED | b'decimal(25,6)' | YES | bytearray(b'') |
| 2 | Date | b'varchar(10)' | NO | bytearray(b'') |
| 32 | Father_node | b'varchar(25)' | YES | bytearray(b'') |
| 10 | GROSS_PROFIT | b'decimal(25,6)' | YES | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 25 | IS_COMP_EPS_ADJUSTED | b'decimal(25,6)' | YES | bytearray(b'') |
| 27 | IS_COMP_SALES | b'decimal(25,6)' | YES | bytearray(b'') |
| 9 | IS_NI_AVAILABLE_TO_COMMON_ADJ | b'decimal(25,6)' | YES | bytearray(b'') |
| 12 | IS_OPER_INC | b'decimal(25,6)' | YES | bytearray(b'') |
| 16 | IS_SGWithA_EXPENSE | b'decimal(25,6)' | YES | bytearray(b'') |
| 26 | IS_SH_FOR_DILUTED_EPS | b'decimal(25,6)' | YES | bytearray(b'') |
| 7 | NET_INCOME | b'decimal(25,6)' | YES | bytearray(b'') |
| 5 | SALES_REV_TURN | b'decimal(25,6)' | YES | bytearray(b'') |
| 18 | SHORT_AND_LONG_TERM_DEBT | b'decimal(25,6)' | YES | bytearray(b'') |
| 3 | Stock_ID | b'varchar(25)' | NO | bytearray(b'') |
| 15 | TOT_COMMON_EQY | b'decimal(25,6)' | YES | bytearray(b'') |
| 30 | TRAIL_12M_CAP_EXPEND | b'decimal(25,6)' | YES | bytearray(b'') |
| 29 | TRAIL_12M_CASH_FROM_OPER | b'decimal(25,6)' | YES | bytearray(b'') |
| 23 | TRAIL_12M_FREE_CASH_FLOW | b'decimal(25,6)' | YES | bytearray(b'') |
| 11 | TRAIL_12M_GROSS_PROFIT | b'decimal(25,6)' | YES | bytearray(b'') |
| 8 | TRAIL_12M_NET_INC | b'decimal(25,6)' | YES | bytearray(b'') |
| 31 | TRAIL_12M_NET_INC_AVAI_COM_SHARE | b'decimal(25,6)' | YES | bytearray(b'') |
| 6 | TRAIL_12M_NET_SALES | b'decimal(25,6)' | YES | bytearray(b'') |
| 13 | TRAIL_12M_OPER_INC | b'decimal(25,6)' | YES | bytearray(b'') |
| 17 | TRAILING_12_MONTH_SGWithA_EXPENSE | b'decimal(25,6)' | YES | bytearray(b'') |
| 33 | Update_time | b'varchar(20)' | NO | bytearray(b'') |



### s05_us_stock_data_copy1 () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 24 | BS_INVENTORIES | b'decimal(25,6)' | YES | bytearray(b'') |
| 14 | BS_TOT_ASSET | b'decimal(25,6)' | YES | bytearray(b'') |
| 19 | BS_TOT_LIAB2 | b'decimal(25,6)' | YES | bytearray(b'') |
| 21 | CAPITAL_EXPEND | b'decimal(25,6)' | YES | bytearray(b'') |
| 22 | CF_CASH_FROM_OPER | b'decimal(25,6)' | YES | bytearray(b'') |
| 28 | CF_FREE_CASH_FLOW | b'decimal(25,6)' | YES | bytearray(b'') |
| 4 | Chi_Name | b'varchar(35)' | YES | bytearray(b'') |
| 20 | CWithCE_AND_STI_DETAILED | b'decimal(25,6)' | YES | bytearray(b'') |
| 2 | Date | b'varchar(10)' | NO | bytearray(b'') |
| 32 | Father_node | b'varchar(25)' | YES | bytearray(b'') |
| 10 | GROSS_PROFIT | b'decimal(25,6)' | YES | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 25 | IS_COMP_EPS_ADJUSTED | b'decimal(25,6)' | YES | bytearray(b'') |
| 27 | IS_COMP_SALES | b'decimal(25,6)' | YES | bytearray(b'') |
| 9 | IS_NI_AVAILABLE_TO_COMMON_ADJ | b'decimal(25,6)' | YES | bytearray(b'') |
| 12 | IS_OPER_INC | b'decimal(25,6)' | YES | bytearray(b'') |
| 16 | IS_SGWithA_EXPENSE | b'decimal(25,6)' | YES | bytearray(b'') |
| 26 | IS_SH_FOR_DILUTED_EPS | b'decimal(25,6)' | YES | bytearray(b'') |
| 7 | NET_INCOME | b'decimal(25,6)' | YES | bytearray(b'') |
| 5 | SALES_REV_TURN | b'decimal(25,6)' | YES | bytearray(b'') |
| 18 | SHORT_AND_LONG_TERM_DEBT | b'decimal(25,6)' | YES | bytearray(b'') |
| 3 | Stock_ID | b'varchar(25)' | NO | bytearray(b'') |
| 15 | TOT_COMMON_EQY | b'decimal(25,6)' | YES | bytearray(b'') |
| 30 | TRAIL_12M_CAP_EXPEND | b'decimal(25,6)' | YES | bytearray(b'') |
| 29 | TRAIL_12M_CASH_FROM_OPER | b'decimal(25,6)' | YES | bytearray(b'') |
| 23 | TRAIL_12M_FREE_CASH_FLOW | b'decimal(25,6)' | YES | bytearray(b'') |
| 11 | TRAIL_12M_GROSS_PROFIT | b'decimal(25,6)' | YES | bytearray(b'') |
| 8 | TRAIL_12M_NET_INC | b'decimal(25,6)' | YES | bytearray(b'') |
| 31 | TRAIL_12M_NET_INC_AVAI_COM_SHARE | b'decimal(25,6)' | YES | bytearray(b'') |
| 6 | TRAIL_12M_NET_SALES | b'decimal(25,6)' | YES | bytearray(b'') |
| 13 | TRAIL_12M_OPER_INC | b'decimal(25,6)' | YES | bytearray(b'') |
| 17 | TRAILING_12_MONTH_SGWithA_EXPENSE | b'decimal(25,6)' | YES | bytearray(b'') |
| 33 | Update_time | b'varchar(20)' | NO | bytearray(b'') |



### s06_onorder () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | direction | b'varchar(20)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 10 | inserttime | b'varchar(20)' | NO | bytearray(b'') |
| 2 | instrumentid | b'varchar(20)' | NO | bytearray(b'') |
| 11 | investorid | b'varchar(20)' | NO | bytearray(b'') |
| 5 | limitprice | b'decimal(30,15)' | NO | bytearray(b'') |
| 12 | localdate | b'datetime(6)' | NO | bytearray(b'') |
| 4 | offsetflag | b'varchar(20)' | NO | bytearray(b'') |
| 13 | orderstatus | b'varchar(1)' | NO | bytearray(b'') |
| 14 | ordersysid | b'varchar(30)' | NO | bytearray(b'') |
| 15 | userid | b'varchar(20)' | NO | bytearray(b'') |
| 6 | volume | b'int(11)' | NO | bytearray(b'') |
| 9 | volumecancled | b'int(11)' | NO | bytearray(b'') |
| 8 | volumeremain | b'int(11)' | NO | bytearray(b'') |
| 7 | volumetraded | b'int(11)' | NO | bytearray(b'') |



### s06_real_time_quotes () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 2 | InstrumentID | b'varchar(15)' | NO | bytearray(b'') |



### s06_tb_emp () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | contract_info | b'varchar(20000)' | NO | bytearray(b'') |
| 2 | contract_name | b'varchar(20)' | NO | bytearray(b'') |
| 4 | contract_using | b'tinyint(1)' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |



### s06_tb_investorid () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 2 | investorid | b'varchar(20)' | NO | bytearray(b'') |



### s06_trading () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | direction_stop | b'longtext' | NO | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 2 | investorid | b'varchar(20)' | NO | bytearray(b'') |
| 3 | ticker | b'varchar(10)' | NO | bytearray(b'') |
| 5 | volumes | b'int(11)' | NO | bytearray(b'') |



### s07_cof_dailyquote_main () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | BBTicker | b'varchar(10)' | YES | bytearray(b'Bloomberg\xe4\xbb\xa3\xe7\xa0\x81') |
| 11 | ClosePrice | b'decimal(18,6)' | YES | bytearray(b'\xe6\x94\xb6\xe7\x9b\x98\xe4\xbb\xb7') |
| 3 | ContractName | b'varchar(50)' | YES | bytearray(b'\xe5\x90\x88\xe7\xba\xa6\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d') |
| 2 | Exchange | b'varchar(10)' | YES | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe6\x89\x80') |
| 6 | ExchangeCode | b'varchar(10)' | YES | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe6\x89\x80\xe4\xbb\xa3\xe7\xa0\x81') |
| 9 | HighPrice | b'decimal(18,6)' | YES | bytearray(b'\xe6\x9c\x80\xe9\xab\x98\xe4\xbb\xb7') |
| 17 | InnerCode | b'int(11)' | YES | bytearray(b'\xe5\x86\x85\xe9\x83\xa8\xe7\xbc\x96\xe7\xa0\x81') |
| 10 | LowPrice | b'decimal(18,6)' | YES | bytearray(b'\xe6\x9c\x80\xe4\xbd\x8e\xe4\xbb\xb7') |
| 18 | MainContractMark | b'int(11)' | YES | bytearray(b'\xe4\xb8\xbb\xe5\x8a\x9b\xe5\x90\x88\xe7\xba\xa6\xe6\xa0\x87\xe8\xaf\x86') |
| 16 | OIChange | b'decimal(18,4)' | YES | bytearray(b'\xe6\x8c\x81\xe4\xbb\x93\xe9\x87\x8f\xe5\x8f\x98\xe5\x8c\x96') |
| 14 | OpenInterest | b'decimal(18,2)' | YES | bytearray(b'\xe6\x8c\x81\xe4\xbb\x93\xe9\x87\x8f') |
| 8 | OpenPrice | b'decimal(18,6)' | YES | bytearray(b'\xe5\xbc\x80\xe7\x9b\x98\xe4\xbb\xb7') |
| 20 | Organization | b'varchar(10)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe5\x8f\x91\xe5\xb8\x83\xe6\x9c\xba\xe6\x9e\x84') |
| 19 | Period | b'varchar(10)' | YES | bytearray(b'\xe9\xa2\x91\xe5\xba\xa6') |
| 7 | PrevSettlePrice | b'decimal(18,6)' | YES | bytearray(b'\xe5\x89\x8d\xe7\xbb\x93\xe7\xae\x97\xe4\xbb\xb7') |
| 12 | SettlePrice | b'decimal(18,6)' | YES | bytearray(b'\xe7\xbb\x93\xe7\xae\x97\xe4\xbb\xb7') |
| 21 | Source | b'varchar(50)' | YES | bytearray(b'\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\xe7\xbd\x91\xe5\x9d\x80') |
| 1 | TradingDay | b'datetime' | NO | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe6\x97\xa5') |
| 15 | Turnover | b'decimal(18,2)' | YES | bytearray(b'\xe6\x88\x90\xe4\xba\xa4\xe9\x87\x91\xe9\xa2\x9d') |
| 22 | Updatetime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 13 | Volume | b'decimal(18,2)' | YES | bytearray(b'\xe6\x88\x90\xe4\xba\xa4\xe9\x87\x8f') |
| 4 | WindCode | b'varchar(20)' | NO | bytearray(b'\xe4\xb8\x87\xe5\xbe\x97\xe4\xbb\xa3\xe7\xa0\x81') |



### s07_contractinfo () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | BBTicker | b'varchar(50)' | YES | bytearray(b'') |
| 9 | ContrSiz | b'int(11)' | YES | bytearray(b'') |
| 2 | Curr | b'varchar(10)' | YES | bytearray(b'') |
| 5 | exch_usym | b'varchar(30)' | YES | bytearray(b'') |
| 10 | exchangecode | b'varchar(40)' | YES | bytearray(b'') |
| 4 | ExchCode | b'varchar(30)' | YES | bytearray(b'') |
| 8 | holdPortfXrate | b'decimal(18,6)' | YES | bytearray(b'') |
| 3 | secu | b'varchar(30)' | YES | bytearray(b'') |
| 1 | Tradingday | b'datetime' | YES | bytearray(b'') |
| 7 | usym | b'varchar(50)' | YES | bytearray(b'') |



### s07_instrument_information () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 26 | BasisPrice | b'double(18,8)' | YES | bytearray(b'') |
| 21 | CreateDate | b'varchar(9)' | YES | bytearray(b'') |
| 14 | Currency | b'varchar(10)' | YES | bytearray(b'') |
| 7 | DeliveryMonth | b'int(2)' | YES | bytearray(b'') |
| 6 | DeliveryYear | b'int(5)' | YES | bytearray(b'') |
| 25 | EndDelivDate | b'varchar(9)' | YES | bytearray(b'') |
| 1 | ExchangeID | b'varchar(20)' | YES | bytearray(b'') |
| 33 | ExchangeRate | b'double(18,8)' | YES | bytearray(b'') |
| 23 | ExpireDate | b'varchar(9)' | YES | bytearray(b'') |
| 4 | InstrumentID | b'varchar(40)' | YES | bytearray(b'') |
| 5 | InstrumentName | b'varchar(30)' | YES | bytearray(b'') |
| 20 | InstrumentStatus | b'varchar(1)' | YES | bytearray(b'') |
| 27 | IsTrading | b'int(1)' | YES | bytearray(b'') |
| 15 | LongPosLimit | b'int(6)' | YES | bytearray(b'') |
| 17 | LowerLimitPrice | b'double(18,8)' | YES | bytearray(b'') |
| 36 | MarginCombType | b'varchar(1)' | YES | bytearray(b'') |
| 8 | MaxLimitOrderVolume | b'int(6)' | YES | bytearray(b'') |
| 10 | MaxMarketOrderVolume | b'int(6)' | YES | bytearray(b'') |
| 9 | MinLimitOrderVolume | b'int(3)' | YES | bytearray(b'') |
| 11 | MinMarketOrderVolume | b'int(3)' | YES | bytearray(b'') |
| 22 | OpenDate | b'varchar(9)' | YES | bytearray(b'') |
| 35 | OptionsMode | b'varchar(1)' | YES | bytearray(b'') |
| 32 | OptionsType | b'varchar(1)' | YES | bytearray(b'') |
| 30 | PositionType | b'varchar(1)' | YES | bytearray(b'') |
| 19 | PreSettlementPrice | b'double(18,8)' | YES | bytearray(b'') |
| 13 | PriceTick | b'double(18,8)' | YES | bytearray(b'') |
| 34 | ProductClass | b'varchar(1)' | YES | bytearray(b'') |
| 2 | ProductID | b'varchar(20)' | YES | bytearray(b'') |
| 3 | ProductName | b'varchar(50)' | YES | bytearray(b'') |
| 16 | ShortPosLimit | b'int(6)' | YES | bytearray(b'') |
| 24 | StartDelivDate | b'varchar(9)' | YES | bytearray(b'') |
| 31 | StrikePrice | b'double(18,8)' | YES | bytearray(b'') |
| 28 | UnderlyingInstrID | b'varchar(31)' | YES | bytearray(b'') |
| 29 | UnderlyingMultiple | b'int(3)' | YES | bytearray(b'') |
| 18 | UpperLimitPrice | b'double(18,8)' | YES | bytearray(b'') |
| 12 | VolumeMultiple | b'int(4)' | YES | bytearray(b'') |



### s07_live_pricing () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | CONTRACTCODE | b'varchar(20)' | YES | bytearray(b'Quantdo Socket Contract Code') |
| 2 | LASTPRICE | b'decimal(18,6)' | YES | bytearray(b'Last price received') |
| 3 | UPDATETIME | b'datetime' | YES | bytearray(b'Last price received time') |



### s07_mapping () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 9 | CUTOFF | b'varchar(50)' | YES | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe6\x97\xa5\xe5\x88\x87\xe6\x8d\xa2\xe6\x97\xb6\xe9\x97\xb4') |
| 1 | EXCHANGE | b'varchar(15)' | YES | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe6\x89\x80') |
| 4 | EXCHANGE_SYMBOL | b'varchar(15)' | YES | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe6\x89\x80\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | FUTURE_OPTION | b'varchar(10)' | YES | bytearray(b'\xe6\x9c\x9f\xe6\x9d\x83/\xe6\x9c\x9f\xe8\xb4\xa7') |
| 5 | IMAGINE | b'varchar(30)' | YES | bytearray(b'Imagine\xe5\x89\x8d\xe7\xbc\x80') |
| 6 | IMAGINE_TYPE | b'varchar(20)' | YES | bytearray(b'Imagine\xe7\xb1\xbb\xe5\x9e\x8b') |
| 3 | INSTRUMENT | b'varchar(50)' | YES | bytearray(b'\xe5\x93\x81\xe7\xa7\x8d') |
| 8 | TIMEZONE_S | b'int(10)' | YES | bytearray(b'\xe5\xa4\x8f\xe4\xbb\xa4\xe6\x97\xb6\xe6\x97\xb6\xe5\xb7\xae') |
| 7 | TIMEZONE_W | b'int(10)' | YES | bytearray(b'\xe5\x86\xac\xe4\xbb\xa4\xe6\x97\xb6\xe6\x97\xb6\xe5\xb7\xae') |



### s07_nav_hist () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | NAVDATE | b'date' | YES | bytearray(b'NAV DATE') |
| 2 | NAVNAME | b'varchar(50)' | YES | bytearray(b'NAV ACCOUNT NAME') |
| 3 | NAVVALUE | b'decimal(18,6)' | YES | bytearray(b'NAV VALUE') |



### s07_onposition () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 9 | AvgCost | b'decimal(18,6)' | YES | bytearray(b'') |
| 6 | BBTicker | b'varchar(50)' | YES | bytearray(b'') |
| 10 | Commission | b'decimal(18,6)' | YES | bytearray(b'') |
| 12 | ContrSiz | b'int(50)' | YES | bytearray(b'') |
| 2 | Curr | b'varchar(10)' | YES | bytearray(b'') |
| 15 | Direction | b'int(5)' | YES | bytearray(b'') |
| 5 | exch_usym | b'varchar(30)' | YES | bytearray(b'') |
| 14 | exchangecode | b'varchar(30)' | NO | bytearray(b'') |
| 4 | ExchCode | b'varchar(30)' | YES | bytearray(b'') |
| 11 | holdPortfXrate | b'decimal(18,6)' | YES | bytearray(b'') |
| 8 | Qty | b'decimal(18,6)' | YES | bytearray(b'') |
| 3 | secu | b'varchar(30)' | YES | bytearray(b'') |
| 13 | SubAcc | b'varchar(50)' | NO | bytearray(b'') |
| 1 | tradingday | b'datetime' | NO | bytearray(b'') |
| 7 | usym | b'varchar(50)' | YES | bytearray(b'') |



### s07_onposition_copy () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 9 | AvgCost | b'decimal(18,6)' | YES | bytearray(b'') |
| 6 | BBTicker | b'varchar(50)' | YES | bytearray(b'') |
| 10 | Commission | b'decimal(18,6)' | YES | bytearray(b'') |
| 12 | ContrSiz | b'int(50)' | YES | bytearray(b'') |
| 2 | Curr | b'varchar(10)' | YES | bytearray(b'') |
| 15 | Direction | b'int(5)' | YES | bytearray(b'') |
| 5 | exch_usym | b'varchar(30)' | YES | bytearray(b'') |
| 14 | exchangecode | b'varchar(30)' | NO | bytearray(b'') |
| 4 | ExchCode | b'varchar(30)' | YES | bytearray(b'') |
| 11 | holdPortfXrate | b'decimal(18,6)' | YES | bytearray(b'') |
| 8 | Qty | b'decimal(18,6)' | YES | bytearray(b'') |
| 3 | secu | b'varchar(30)' | YES | bytearray(b'') |
| 13 | SubAcc | b'varchar(50)' | NO | bytearray(b'') |
| 1 | tradingday | b'datetime' | NO | bytearray(b'') |
| 7 | usym | b'varchar(50)' | YES | bytearray(b'') |



### s07_ontrade () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 17 | BaseCurrency | b'varchar(10)' | YES | bytearray(b'\xe5\x9f\xba\xe5\x87\x86\xe8\xb4\xa7\xe5\xb8\x81') |
| 5 | BBTicker | b'varchar(20)' | YES | bytearray(b'BBG\xe4\xbb\xa3\xe7\xa0\x81') |
| 22 | BrokerID | b'varchar(20)' | YES | bytearray(b'\xe7\xbb\x8f\xe7\xba\xaa\xe5\x95\x86\xe6\xa0\x87\xe8\xaf\x86') |
| 26 | CCY1 | b'varchar(20)' | YES | bytearray(b'') |
| 27 | CCY1N | b'decimal(30,16)' | YES | bytearray(b'') |
| 28 | CCY2 | b'varchar(20)' | YES | bytearray(b'') |
| 29 | CCY2N | b'decimal(30,16)' | YES | bytearray(b'') |
| 16 | Commision | b'decimal(10,6)' | YES | bytearray(b'\xe6\x89\x8b\xe7\xbb\xad\xe8\xb4\xb9') |
| 3 | ContractName | b'varchar(10)' | YES | bytearray(b'\xe5\x90\x88\xe7\xba\xa6\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d') |
| 12 | Direction | b'varchar(20)' | YES | bytearray(b'\xe6\x88\x90\xe4\xba\xa4\xe6\x96\xb9\xe5\x90\x91') |
| 37 | email_title | b'varchar(200)' | YES | bytearray(b'') |
| 2 | Exchange | b'varchar(10)' | YES | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe6\x89\x80') |
| 6 | ExchangeCode | b'varchar(30)' | YES | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe6\x89\x80\xe4\xbb\xa3\xe7\xa0\x81') |
| 18 | ExcuTime | b'datetime' | YES | bytearray(b'\xe6\x88\x90\xe4\xba\xa4\xe6\x97\xb6\xe9\x97\xb4') |
| 36 | Expiry | b'datetime' | YES | bytearray(b'') |
| 31 | FixDate | b'datetime' | YES | bytearray(b'') |
| 34 | FWD_points | b'decimal(30,16)' | YES | bytearray(b'') |
| 7 | IMGcode | b'varchar(20)' | YES | bytearray(b'') |
| 8 | InnerCode | b'int(11)' | YES | bytearray(b'\xe5\x86\x85\xe9\x83\xa8\xe7\xbc\x96\xe7\xa0\x81') |
| 20 | InvestorID | b'varchar(20)' | YES | bytearray(b'\xe8\xb4\xa6\xe6\x88\xb7\xe6\xa0\x87\xe8\xaf\x86') |
| 14 | Lastprice | b'decimal(30,16)' | YES | bytearray(b'\xe6\x88\x90\xe4\xba\xa4\xe4\xbb\xb7') |
| 38 | LocalDate | b'datetime' | YES | bytearray(b'\xe6\x9c\xac\xe5\x9c\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 9 | MainContractMark | b'int(11)' | YES | bytearray(b'\xe4\xb8\xbb\xe5\x8a\x9b\xe5\x90\x88\xe7\xba\xa6\xe6\xa0\x87\xe8\xaf\x86') |
| 13 | Offset | b'varchar(20)' | YES | bytearray(b'\xe5\xbc\x80\xe5\xb9\xb3\xe4\xbb\x93\xe6\xa0\x87\xe8\xaf\x86') |
| 11 | OrderID | b'varchar(20)' | YES | bytearray(b'\xe5\xa7\x94\xe6\x89\x98\xe7\xbc\x96\xe5\x8f\xb7') |
| 32 | Rate | b'decimal(30,16)' | YES | bytearray(b'') |
| 33 | Spot | b'decimal(30,16)' | YES | bytearray(b'') |
| 19 | StrategyID | b'varchar(20)' | YES | bytearray(b'\xe7\xad\x96\xe7\x95\xa5\xe6\xa0\x87\xe8\xaf\x86') |
| 10 | TradeID | b'varchar(20)' | NO | bytearray(b'\xe6\x88\x90\xe4\xba\xa4\xe7\xbc\x96\xe5\x8f\xb7') |
| 21 | Trader | b'varchar(20)' | YES | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe5\x91\x98') |
| 1 | TradingDay | b'datetime' | NO | bytearray(b'\xe6\xb5\x9c\xe3\x82\x86\xe6\xa7\x97\xe9\x8f\x83?') |
| 24 | Type | b'varchar(20)' | YES | bytearray(b'') |
| 25 | Underlying | b'varchar(20)' | YES | bytearray(b'') |
| 23 | UpdateTime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |
| 35 | Value | b'decimal(30,16)' | YES | bytearray(b'') |
| 30 | ValueDate | b'datetime' | YES | bytearray(b'') |
| 15 | Volume | b'decimal(18,2)' | YES | bytearray(b'\xe6\x88\x90\xe4\xba\xa4\xe9\x87\x8f') |
| 4 | WindCode | b'varchar(10)' | YES | bytearray(b'\xe4\xb8\x87\xe5\xbe\x97\xe4\xbb\xa3\xe7\xa0\x81') |



### s07_pnl () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 8 | AvgCost | b'decimal(18,8)' | YES | bytearray(b'') |
| 6 | PnlValue | b'decimal(18,8)' | NO | bytearray(b'\xe9\x8d\x91\xe2\x82\xac\xe9\x8d\x8a?') |
| 7 | Qty | b'decimal(18,2)' | YES | bytearray(b'') |
| 3 | StrID | b'varchar(50)' | YES | bytearray(b'\xe7\xad\x96\xe7\x95\xa5\xe6\xa0\x87\xe8\xaf\x86') |
| 4 | SubAcc | b'varchar(50)' | YES | bytearray(b'\xe5\xad\x90\xe8\xb4\xa6\xe6\x88\xb7\xe6\xa0\x87\xe8\xaf\x86') |
| 2 | Symbol | b'varchar(20)' | NO | bytearray(b'\xe9\x96\xb8\xe6\xbf\x85\xe8\x83\xb6\xe9\xa1\xab\xe6\x8e\x93\xe7\xa6\x92\xe9\x94\x9d\xe5\x9b\xa9\xe5\x9e\xb3') |
| 5 | Trader | b'varchar(30)' | YES | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe5\x91\x98\xe6\xa0\x87\xe8\xaf\x86') |
| 1 | Tradingday | b'datetime' | NO | bytearray(b'\xe6\xb5\x9c\xe3\x82\x86\xe6\xa7\x97\xe9\x8f\x83?') |



### s07_pnl_img () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 22 | ACCT | b'varchar(50)' | YES | bytearray(b'\xe5\xad\x90\xe8\xb4\xa6\xe6\x88\xb7\xe4\xbf\xa1\xe6\x81\xaf') |
| 16 | AVGCOST | b'decimal(18,6)' | YES | bytearray(b'\xe5\x90\x88\xe7\xba\xa6\xe5\xb9\xb3\xe5\x9d\x87\xe6\x88\x90\xe6\x9c\xac') |
| 3 | BBGTICKER | b'varchar(50)' | YES | bytearray(b'Bloomberg\xe5\x90\x88\xe7\xba\xa6\xe4\xbb\xa3\xe7\xa0\x81') |
| 18 | CONTRACTMUL | b'decimal(18,6)' | YES | bytearray(b'\xe5\x90\x88\xe7\xba\xa6\xe4\xb9\x98\xe6\x95\xb0') |
| 14 | CURRENCY | b'varchar(10)' | YES | bytearray(b'\xe5\x90\x88\xe7\xba\xa6\xe8\xb4\xa7\xe5\xb8\x81') |
| 8 | DAY_PNL | b'decimal(18,6)' | YES | bytearray(b'\xe5\xbd\x93\xe6\x97\xa5PnL') |
| 9 | DAY_RLZD | b'decimal(18,6)' | YES | bytearray(b'\xe5\xbd\x93\xe6\x97\xa5\xe5\xb7\xb2\xe5\xae\x9e\xe7\x8e\xb0PnL') |
| 10 | DAY_URLZD | b'decimal(18,6)' | YES | bytearray(b'\xe5\xbd\x93\xe6\x97\xa5\xe6\x9c\xaa\xe5\xae\x9e\xe7\x8e\xb0PnL') |
| 7 | EXCHANGE | b'varchar(50)' | YES | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe6\x89\x80\xe4\xbb\xa3\xe7\xa0\x81') |
| 4 | EXCHCODE | b'varchar(50)' | YES | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe6\x89\x80\xe5\x90\x88\xe7\xba\xa6\xe4\xbb\xa3\xe7\xa0\x81') |
| 12 | MTD_PNL | b'decimal(18,6)' | YES | bytearray(b'MTD\xe6\x80\xbbPnL') |
| 1 | PNLDATE | b'datetime' | YES | bytearray(b'PnL\xe6\x97\xa5\xe6\x9c\x9f') |
| 19 | PORTFXRATE | b'decimal(18,6)' | YES | bytearray(b'\xe6\xb1\x87\xe7\x8e\x87\xe4\xb9\x98\xe6\x95\xb0') |
| 5 | QDCODE | b'varchar(50)' | YES | bytearray(b'\xe9\x87\x8f\xe6\x8a\x95\xe5\x90\x88\xe7\xba\xa6\xe4\xbb\xa3\xe7\xa0\x81') |
| 6 | QDTICKER | b'varchar(50)' | YES | bytearray(b'\xe9\x87\x8f\xe6\x8a\x95\xe5\x90\x88\xe7\xba\xa6\xe4\xbb\xa3\xe7\xa0\x81\xe5\x8f\x8a\xe4\xba\xa4\xe6\x98\x93\xe6\x89\x80\xe4\xbb\xa3\xe7\xa0\x81') |
| 15 | QUANTITY | b'decimal(18,6)' | YES | bytearray(b'\xe5\x90\x88\xe7\xba\xa6\xe6\x8c\x81\xe4\xbb\x93\xe6\x95\xb0\xe9\x87\x8f') |
| 2 | SECURI | b'varchar(50)' | YES | bytearray(b'Imagine\xe5\x90\x88\xe7\xba\xa6\xe5\x90\x8d\xe7\xa7\xb0\xe4\xbb\xa3\xe7\xa0\x81') |
| 20 | STRATEGY | b'varchar(20)' | YES | bytearray(b'\xe7\xad\x96\xe7\x95\xa5\xe6\xa0\x87\xe7\xad\xbe') |
| 21 | SYLEVERAGE | b'decimal(18,6)' | YES | bytearray(b'\xe6\x8c\x81\xe4\xbb\x93\xe5\xb8\x82\xe5\x80\xbc\xe6\x9d\xa0\xe6\x9d\x86') |
| 17 | USYM | b'varchar(20)' | YES | bytearray(b'\xe5\x90\x88\xe7\xba\xa6\xe6\xa0\x87\xe7\x9a\x84\xe4\xbb\xa3\xe7\xa0\x81') |
| 11 | WTD_PNL | b'decimal(18,6)' | YES | bytearray(b'WTD\xe6\x80\xbbPnL') |
| 13 | YTD_PNL | b'decimal(18,6)' | YES | bytearray(b'YTD\xe6\x80\xbbPnL') |



### s07_pnl_img_os () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 22 | ACCT | b'varchar(50)' | YES | bytearray(b'\xe5\xad\x90\xe8\xb4\xa6\xe6\x88\xb7\xe4\xbf\xa1\xe6\x81\xaf') |
| 16 | AVGCOST | b'decimal(18,6)' | YES | bytearray(b'\xe5\x90\x88\xe7\xba\xa6\xe5\xb9\xb3\xe5\x9d\x87\xe6\x88\x90\xe6\x9c\xac') |
| 3 | BBGTICKER | b'varchar(50)' | YES | bytearray(b'Bloomberg\xe5\x90\x88\xe7\xba\xa6\xe4\xbb\xa3\xe7\xa0\x81') |
| 18 | CONTRACTMUL | b'decimal(18,6)' | YES | bytearray(b'\xe5\x90\x88\xe7\xba\xa6\xe4\xb9\x98\xe6\x95\xb0') |
| 14 | CURRENCY | b'varchar(10)' | YES | bytearray(b'\xe5\x90\x88\xe7\xba\xa6\xe8\xb4\xa7\xe5\xb8\x81') |
| 8 | DAY_PNL | b'decimal(18,6)' | YES | bytearray(b'\xe5\xbd\x93\xe6\x97\xa5PnL') |
| 9 | DAY_RLZD | b'decimal(18,6)' | YES | bytearray(b'\xe5\xbd\x93\xe6\x97\xa5\xe5\xb7\xb2\xe5\xae\x9e\xe7\x8e\xb0PnL') |
| 10 | DAY_URLZD | b'decimal(18,6)' | YES | bytearray(b'\xe5\xbd\x93\xe6\x97\xa5\xe6\x9c\xaa\xe5\xae\x9e\xe7\x8e\xb0PnL') |
| 7 | EXCHANGE | b'varchar(50)' | YES | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe6\x89\x80\xe4\xbb\xa3\xe7\xa0\x81') |
| 4 | EXCHCODE | b'varchar(50)' | YES | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe6\x89\x80\xe5\x90\x88\xe7\xba\xa6\xe4\xbb\xa3\xe7\xa0\x81') |
| 12 | MTD_PNL | b'decimal(18,6)' | YES | bytearray(b'MTD\xe6\x80\xbbPnL') |
| 1 | PNLDATE | b'date' | YES | bytearray(b'PnL\xe6\x97\xa5\xe6\x9c\x9f') |
| 19 | PORTFXRATE | b'decimal(18,6)' | YES | bytearray(b'\xe6\xb1\x87\xe7\x8e\x87\xe4\xb9\x98\xe6\x95\xb0') |
| 5 | QDCODE | b'varchar(50)' | YES | bytearray(b'\xe9\x87\x8f\xe6\x8a\x95\xe5\x90\x88\xe7\xba\xa6\xe4\xbb\xa3\xe7\xa0\x81') |
| 6 | QDTICKER | b'varchar(50)' | YES | bytearray(b'\xe9\x87\x8f\xe6\x8a\x95\xe5\x90\x88\xe7\xba\xa6\xe4\xbb\xa3\xe7\xa0\x81\xe5\x8f\x8a\xe4\xba\xa4\xe6\x98\x93\xe6\x89\x80\xe4\xbb\xa3\xe7\xa0\x81') |
| 15 | QUANTITY | b'decimal(18,6)' | YES | bytearray(b'\xe5\x90\x88\xe7\xba\xa6\xe6\x8c\x81\xe4\xbb\x93\xe6\x95\xb0\xe9\x87\x8f') |
| 2 | SECURI | b'varchar(50)' | YES | bytearray(b'Imagine\xe5\x90\x88\xe7\xba\xa6\xe5\x90\x8d\xe7\xa7\xb0\xe4\xbb\xa3\xe7\xa0\x81') |
| 20 | STRATEGY | b'varchar(20)' | YES | bytearray(b'\xe7\xad\x96\xe7\x95\xa5\xe6\xa0\x87\xe7\xad\xbe') |
| 21 | SYLEVERAGE | b'decimal(18,6)' | YES | bytearray(b'\xe6\x8c\x81\xe4\xbb\x93\xe5\xb8\x82\xe5\x80\xbc\xe6\x9d\xa0\xe6\x9d\x86') |
| 17 | USYM | b'varchar(20)' | YES | bytearray(b'\xe5\x90\x88\xe7\xba\xa6\xe6\xa0\x87\xe7\x9a\x84\xe4\xbb\xa3\xe7\xa0\x81') |
| 11 | WTD_PNL | b'decimal(18,6)' | YES | bytearray(b'WTD\xe6\x80\xbbPnL') |
| 13 | YTD_PNL | b'decimal(18,6)' | YES | bytearray(b'YTD\xe6\x80\xbbPnL') |



### s07_pnl_spec () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | SPECNAME | b'varchar(20)' | YES | bytearray(b'Spec Name') |
| 2 | SPECVALUE | b'decimal(18,6)' | YES | bytearray(b'Spec Value') |



### s07_settleposition () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 9 | AvgCost | b'decimal(18,6)' | YES | bytearray(b'') |
| 6 | BBTicker | b'varchar(50)' | YES | bytearray(b'') |
| 10 | Commission | b'decimal(18,6)' | YES | bytearray(b'') |
| 12 | ContrSiz | b'int(50)' | YES | bytearray(b'') |
| 2 | Curr | b'varchar(10)' | YES | bytearray(b'') |
| 15 | Direction | b'int(5)' | YES | bytearray(b'') |
| 5 | exch_usym | b'varchar(30)' | YES | bytearray(b'') |
| 14 | exchangecode | b'varchar(30)' | YES | bytearray(b'') |
| 4 | ExchCode | b'varchar(30)' | YES | bytearray(b'') |
| 11 | holdPortfXrate | b'decimal(18,6)' | YES | bytearray(b'') |
| 8 | Qty | b'decimal(18,6)' | YES | bytearray(b'') |
| 3 | secu | b'varchar(30)' | YES | bytearray(b'') |
| 13 | SubAcc | b'varchar(50)' | YES | bytearray(b'') |
| 1 | tradingday | b'datetime' | YES | bytearray(b'') |
| 7 | usym | b'varchar(50)' | YES | bytearray(b'') |



### s07_str_parameter () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 3 | Par_Var | b'varchar(20)' | YES | bytearray(b'\xe5\x8f\x82\xe6\x95\xb0\xe5\x92\x8c\xe5\x8f\x98\xe9\x87\x8f') |
| 2 | Status | b'varchar(20)' | YES | bytearray(b'\xe7\x8a\xb6\xe6\x80\x81') |
| 4 | UpdateTime | b'datetime' | YES | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s07_ticker_mapping () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | BLOOMBERG | b'varchar(50)' | YES | bytearray(b'Bloomberg Ticker') |
| 2 | EXCHANGE | b'varchar(50)' | YES | bytearray(b'Exchange Symbol') |
| 5 | EXCHCODE | b'varchar(10)' | YES | bytearray(b'Exchange') |
| 4 | IMAGINE | b'varchar(50)' | YES | bytearray(b'Imagine Security ID') |
| 1 | QUANTDO | b'varchar(50)' | YES | bytearray(b'QuantDo Ticker') |
| 6 | TICKERTYPE | b'varchar(50)' | YES | bytearray(b'Generic vs Actual') |



### s09_bbg_mapping () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | bbgTicker | b'varchar(50)' | YES | bytearray(b'') |
| 2 | bbgType | b'varchar(50)' | YES | bytearray(b'') |
| 4 | LME | b'int(11)' | YES | bytearray(b'') |
| 3 | Prefix | b'varchar(50)' | YES | bytearray(b'') |



### s09_bbg_security (BBG行情映射表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | DestSymbol | b'varchar(50)' | YES | bytearray(b'Imagine\xe7\x9a\x84security') |



### s09_bbgquote () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | datetime | b'date' | NO | bytearray(b'') |
| 4 | HIGH | b'double' | YES | bytearray(b'') |
| 5 | LOW | b'double' | YES | bytearray(b'') |
| 3 | OPEN | b'double' | YES | bytearray(b'') |
| 8 | OPEN_INT | b'int(11)' | YES | bytearray(b'') |
| 10 | PX_ASK | b'double' | YES | bytearray(b'') |
| 9 | PX_BID | b'double' | YES | bytearray(b'') |
| 6 | PX_LAST | b'double' | YES | bytearray(b'') |
| 1 | Ticker | b'varchar(255)' | YES | bytearray(b'') |
| 7 | VOLUME | b'double' | YES | bytearray(b'') |



### s09_cn_stock_data () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | BillReceivable | b'decimal(19,4)' | YES | bytearray(b'\xe5\xba\x94\xe6\x94\xb6\xe7\xa5\xa8\xe6\x8d\xae') |
| 5 | CashEquivalents | b'decimal(19,4)' | YES | bytearray(b'\xe8\xb4\xa7\xe5\xb8\x81\xe8\xb5\x84\xe9\x87\x91') |
| 22 | Data | b'decimal(19,4)' | YES | bytearray(b'\xe8\x87\xaa\xe7\x94\xb1\xe7\x8e\xb0\xe9\x87\x91\xe6\xb5\x81\xe9\x87\x8f\xef\xbc\x88\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe5\xbc\x8f_\xe5\xbe\x85\xe8\x8e\xb7\xe5\xbe\x97\xef\xbc\x89') |
| 1 | Date | b'varchar(10)' | NO | bytearray(b'\xe6\x97\xa5\xe6\x9c\x9f') |
| 23 | Father_node | b'varchar(12)' | NO | bytearray(b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0') |
| 20 | FCFF | b'decimal(19,4)' | YES | bytearray(b'\xe4\xbc\x81\xe4\xb8\x9a\xe8\x87\xaa\xe7\x94\xb1\xe7\x8e\xb0\xe9\x87\x91\xe6\xb5\x81\xe9\x87\x8f\xef\xbc\x88FCFF\xef\xbc\x89') |
| 9 | FixIntanOtherAssetAcquiCash | b'decimal(19,4)' | YES | bytearray(b'\xe5\x8d\x95\xe5\xad\xa3\xe5\xba\xa6.\xe8\xb4\xad\xe5\xbb\xba\xe5\x9b\xba\xe5\xae\x9a\xe8\xb5\x84\xe4\xba\xa7\xe3\x80\x81\xe6\x97\xa0\xe5\xbd\xa2\xe8\xb5\x84\xe4\xba\xa7\xe5\x92\x8c\xe5\x85\xb6\xe4\xbb\x96\xe9\x95\xbf\xe6\x9c\x9f\xe8\xb5\x84\xe4\xba\xa7\xe6\x94\xaf\xe4\xbb\x98\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91') |
| 19 | GrossProfitTTM | b'decimal(19,4)' | YES | bytearray(b'\xe6\xaf\x9b\xe5\x88\xa9\xef\xbc\x88TTM\xef\xbc\x89') |
| 18 | InterestBearDebt | b'decimal(19,4)' | YES | bytearray(b'\xe5\xb8\xa6\xe6\x81\xaf\xe5\x80\xba\xe5\x8a\xa1') |
| 7 | Inventories | b'decimal(19,4)' | YES | bytearray(b'\xe5\xad\x98\xe8\xb4\xa7') |
| 17 | NetOperateCashFlowTTM | b'decimal(19,4)' | YES | bytearray(b'\xe7\xbb\x8f\xe8\x90\xa5\xe6\xb4\xbb\xe5\x8a\xa8\xe7\x8e\xb0\xe9\x87\x91\xe5\x87\x80\xe6\xb5\x81\xe9\x87\x8f(TTM)') |
| 14 | NetProfitCut | b'decimal(19,4)' | YES | bytearray(b'\xe6\x89\xa3\xe9\x99\xa4\xe9\x9d\x9e\xe7\xbb\x8f\xe5\xb8\xb8\xe6\x80\xa7\xe6\x8d\x9f\xe7\x9b\x8a\xe5\x90\x8e\xe7\x9a\x84\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6\xef\xbc\x88\xe9\x9d\x9eTTM\xef\xbc\x89\xe8\xae\xa1\xe7\xae\x97\xe6\x96\xb9\xe5\xbc\x8f\xe5\xbe\x85\xe8\x8e\xb7\xe5\xbe\x97') |
| 11 | NPFromParentCompanyOwners | b'decimal(19,4)' | YES | bytearray(b'\xe5\x8d\x95\xe5\xad\xa3\xe5\xba\xa6.\xe5\xbd\x92\xe5\xb1\x9e\xe6\xaf\x8d\xe5\x85\xac\xe5\x8f\xb8\xe8\x82\xa1\xe4\xb8\x9c\xe7\x9a\x84\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6') |
| 16 | NPParentCompanyOwnersTTM | b'decimal(19,4)' | YES | bytearray(b'\xe5\xbd\x92\xe5\xb1\x9e\xe6\xaf\x8d\xe5\x85\xac\xe5\x8f\xb8\xe8\x82\xa1\xe4\xb8\x9c\xe7\x9a\x84\xe5\x87\x80\xe5\x88\xa9\xe6\xb6\xa6\xef\xbc\x88TTM\xef\xbc\x89') |
| 10 | OperatingRevenue | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5') |
| 15 | OperatingRevenueTTM | b'decimal(19,4)' | YES | bytearray(b'\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5\xef\xbc\x88TTM\xef\xbc\x89') |
| 21 | qfa_grossmargin | b'decimal(19,4)' | YES | bytearray(b'\xe5\x8d\x95\xe5\xad\xa3\xe5\xba\xa6.\xe6\xaf\x9b\xe5\x88\xa9') |
| 12 | qfa_OperatingRevenue | b'decimal(19,4)' | YES | bytearray(b'\xe5\x8d\x95\xe5\xad\xa3\xe5\xba\xa6.\xe8\x90\xa5\xe4\xb8\x9a\xe6\x94\xb6\xe5\x85\xa5') |
| 8 | SEWithoutMI | b'decimal(19,4)' | YES | bytearray(b'\xe5\xbd\x92\xe5\xb1\x9e\xe6\xaf\x8d\xe5\x85\xac\xe5\x8f\xb8\xe8\x82\xa1\xe4\xb8\x9c\xe7\x9a\x84\xe6\x9d\x83\xe7\x9b\x8a') |
| 2 | Stock_ID | b'varchar(10)' | NO | bytearray(b'\xe8\x82\xa1\xe6\x8c\x87\xe5\x90\x8d\xe7\xa7\xb0') |
| 4 | TotalAssets | b'decimal(19,4)' | YES | bytearray(b'\xe8\xb5\x84\xe4\xba\xa7\xe6\x80\xbb\xe8\xae\xa1') |
| 3 | TotalLiability | b'decimal(19,4)' | YES | bytearray(b'\xe8\xb4\x9f\xe5\x80\xba\xe5\x90\x88\xe8\xae\xa1') |
| 13 | TotalMV | b'decimal(19,4)' | YES | bytearray(b'\xe6\x80\xbb\xe5\xb8\x82\xe5\x80\xbc2') |
| 24 | Update_time | b'varchar(20)' | NO | bytearray(b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4') |



### s09_contract_spec () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 8 | BLOOMBERG | b'varchar(50)' | YES | bytearray(b'') |
| 4 | CONTRACTMUL | b'decimal(10,0)' | YES | bytearray(b'') |
| 3 | CURR | b'varchar(50)' | YES | bytearray(b'') |
| 1 | EXCHANGE | b'varchar(50)' | YES | bytearray(b'') |
| 10 | EXCHCODE | b'varchar(50)' | YES | bytearray(b'') |
| 9 | IMAGINE | b'varchar(50)' | YES | bytearray(b'') |
| 5 | PORTFXRATE | b'decimal(10,0)' | YES | bytearray(b'') |
| 7 | QUANTDO | b'varchar(50)' | YES | bytearray(b'') |
| 6 | STRATEGY | b'varchar(50)' | YES | bytearray(b'') |
| 2 | USYM | b'varchar(50)' | YES | bytearray(b'') |



### s09_contractmul () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | Description | b'varchar(255)' | YES | bytearray(b'') |
| 3 | Mul | b'double' | YES | bytearray(b'') |
| 1 | Ticker | b'varchar(255)' | YES | bytearray(b'') |



### s09_cotd () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | Date | b'varchar(255)' | YES | bytearray(b'') |
| 3 | Fields | b'varchar(255)' | YES | bytearray(b'') |
| 1 | Ticker | b'varchar(255)' | YES | bytearray(b'') |
| 4 | Values | b'double' | YES | bytearray(b'') |



### s09_cott () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Ticker | b'varchar(255)' | YES | bytearray(b'') |



### s09_cu_w () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | date | b'double' | YES | bytearray(b'') |
| 2 | oi_AA1 | b'int(11)' | YES | bytearray(b'') |
| 3 | oi_CL1 | b'int(11)' | YES | bytearray(b'') |
| 4 | oi_CU1 | b'int(11)' | YES | bytearray(b'') |
| 5 | oi_CU2 | b'int(11)' | YES | bytearray(b'') |
| 6 | oi_GC1 | b'int(11)' | YES | bytearray(b'') |
| 7 | oi_HG1 | b'int(11)' | YES | bytearray(b'') |
| 8 | oi_HG2 | b'int(11)' | YES | bytearray(b'') |
| 9 | oi_LMCADS03 | b'int(11)' | YES | bytearray(b'') |
| 10 | oi_LMCADY | b'int(11)' | YES | bytearray(b'') |
| 11 | oi_PBL1 | b'int(11)' | YES | bytearray(b'') |
| 12 | oi_SP1 | b'int(11)' | YES | bytearray(b'') |
| 13 | oi_XII1 | b'int(11)' | YES | bytearray(b'') |
| 14 | oi_ZNA1 | b'int(11)' | YES | bytearray(b'') |
| 15 | p_.CMXCUS1 | b'double' | YES | bytearray(b'') |
| 16 | p_.LMECUS1 | b'double' | YES | bytearray(b'') |
| 17 | p_.SHCMXCU | b'double' | YES | bytearray(b'') |
| 18 | p_.SHCU_3.0 | b'double' | YES | bytearray(b'') |
| 19 | p_.SHCU_3.1 | b'double' | YES | bytearray(b'') |
| 20 | p_.SHCUAL1 | b'double' | YES | bytearray(b'') |
| 21 | p_.SHLME_CU | b'double' | YES | bytearray(b'') |
| 22 | p_AA1 | b'double' | YES | bytearray(b'') |
| 23 | p_CCSMCUG1 | b'double' | YES | bytearray(b'') |
| 24 | p_CL1 | b'double' | YES | bytearray(b'') |
| 25 | p_CU1 | b'double' | YES | bytearray(b'') |
| 26 | p_CU2 | b'double' | YES | bytearray(b'') |
| 27 | p_GC1 | b'double' | YES | bytearray(b'') |
| 28 | p_HG1 | b'double' | YES | bytearray(b'') |
| 29 | p_HG2 | b'double' | YES | bytearray(b'') |
| 30 | p_LMCADS03 | b'double' | YES | bytearray(b'') |
| 31 | p_LMCADY | b'double' | YES | bytearray(b'') |
| 32 | p_PBL1 | b'double' | YES | bytearray(b'') |
| 33 | p_SHSZ300 | b'double' | YES | bytearray(b'') |
| 34 | p_SP1 | b'double' | YES | bytearray(b'') |
| 35 | p_USDCNY | b'double' | YES | bytearray(b'') |
| 36 | p_USGG10 | b'double' | YES | bytearray(b'') |
| 37 | p_XII1 | b'double' | YES | bytearray(b'') |
| 38 | p_ZNA1 | b'double' | YES | bytearray(b'') |
| 39 | vl_AA1 | b'double' | YES | bytearray(b'') |
| 40 | vl_CL1 | b'double' | YES | bytearray(b'') |
| 41 | vl_CU1 | b'double' | YES | bytearray(b'') |
| 42 | vl_CU2 | b'double' | YES | bytearray(b'') |
| 43 | vl_GC1 | b'double' | YES | bytearray(b'') |
| 44 | vl_HG1 | b'double' | YES | bytearray(b'') |
| 45 | vl_HG2 | b'double' | YES | bytearray(b'') |
| 46 | vl_LMCADS03 | b'double' | YES | bytearray(b'') |
| 47 | vl_LMCADY | b'double' | YES | bytearray(b'') |
| 48 | vl_PBL1 | b'double' | YES | bytearray(b'') |
| 49 | vl_SHSZ300 | b'double' | YES | bytearray(b'') |
| 50 | vl_SP1 | b'double' | YES | bytearray(b'') |
| 51 | vl_USGG10 | b'double' | YES | bytearray(b'') |
| 52 | vl_XII1 | b'double' | YES | bytearray(b'') |
| 53 | vl_ZNA1 | b'double' | YES | bytearray(b'') |



### s09_da_fut_market (期货行情数据) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 13 | ClosePrice | b'decimal(19,4)' | YES | bytearray(b'\xe6\x94\xb6\xe7\x9b\x98\xe4\xbb\xb7') |
| 8 | Cont1 | b'varchar(50)' | YES | bytearray(b'\xe8\xbf\x9e1') |
| 1 | Enddate | b'datetime' | NO | bytearray(b'\xe6\x88\x90\xe4\xba\xa4\xe6\x97\xa5\xe6\x9c\x9f') |
| 2 | Exchange | b'int(11)' | NO | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe6\x89\x80\xe4\xbb\xa3\xe7\xa0\x81') |
| 11 | HighPrice | b'decimal(19,4)' | YES | bytearray(b'\xe6\x9c\x80\xe9\xab\x98\xe4\xbb\xb7') |
| 12 | LowPrice | b'decimal(19,4)' | YES | bytearray(b'\xe6\x9c\x80\xe4\xbd\x8e\xe4\xbb\xb7') |
| 5 | M_SettlementDate | b'datetime' | YES | bytearray(b'\xe4\xb8\xbb\xe5\x8a\x9b\xe5\x90\x88\xe7\xba\xa6\xe5\x88\xb0\xe6\x9c\x9f\xe6\x97\xa5') |
| 4 | Main | b'varchar(50)' | YES | bytearray(b'\xe4\xb8\xbb\xe5\x8a\x9b\xe5\x90\x88\xe7\xba\xa6') |
| 16 | OpenInterest | b'int(18)' | YES | bytearray(b'\xe6\x8c\x81\xe4\xbb\x93\xe9\x87\x8f(\xe6\x89\x8b)') |
| 10 | OpenPrice | b'decimal(19,4)' | YES | bytearray(b'\xe5\xbc\x80\xe7\x9b\x98\xe4\xbb\xb7') |
| 3 | OptionCode | b'int(11)' | NO | bytearray(b'\xe5\x93\x81\xe7\xa7\x8d\xe4\xbb\xa3\xe7\xa0\x81') |
| 14 | SettlePrice | b'decimal(19,4)' | YES | bytearray(b'\xe7\xbb\x93\xe7\xae\x97\xe4\xbb\xb7') |
| 7 | SM_SettlementDate | b'datetime' | YES | bytearray(b'\xe6\xac\xa1\xe4\xb8\xbb\xe5\x8a\x9b\xe5\x90\x88\xe7\xba\xa6\xe5\x88\xb0\xe6\x9c\x9f\xe6\x97\xa5') |
| 6 | SMain | b'varchar(50)' | YES | bytearray(b'\xe6\xac\xa1\xe4\xb8\xbb\xe5\x8a\x9b\xe5\x90\x88\xe7\xba\xa6') |
| 9 | SMain_Settle | b'decimal(19,4)' | YES | bytearray(b'\xe5\x85\x88\xe7\xbb\x93\xe7\xae\x97\xe4\xbb\xb7') |
| 17 | Turnover | b'decimal(19,4)' | YES | bytearray(b'\xe6\x88\x90\xe4\xba\xa4\xe9\xa2\x9d') |
| 15 | Volume | b'int(18)' | YES | bytearray(b'\xe6\x88\x90\xe4\xba\xa4\xe9\x87\x8f(\xe6\x89\x8b)') |



### s09_dataview_pro () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | id | b'int(11)' | NO | bytearray(b'') |



### s09_em_ccy () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 2 | DXY_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | USDBRL_PX_LAST | b'double' | YES | bytearray(b'') |
| 4 | USDCLP_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | USDCNH_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | USDCOP_PX_LAST | b'double' | YES | bytearray(b'') |
| 7 | USDCZK_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | USDHUF_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | USDIDR_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | USDILS_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | USDINR_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | USDKRW_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | USDMXN_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | USDMYR_PX_LAST | b'double' | YES | bytearray(b'') |
| 15 | USDPHP_PX_LAST | b'double' | YES | bytearray(b'') |
| 16 | USDPLN_PX_LAST | b'double' | YES | bytearray(b'') |
| 17 | USDRON_PX_LAST | b'double' | YES | bytearray(b'') |
| 18 | USDRUB_PX_LAST | b'double' | YES | bytearray(b'') |
| 19 | USDSGD_PX_LAST | b'double' | YES | bytearray(b'') |
| 20 | USDTHB_PX_LAST | b'double' | YES | bytearray(b'') |
| 21 | USDTRY_PX_LAST | b'double' | YES | bytearray(b'') |
| 22 | USDTWD_PX_LAST | b'double' | YES | bytearray(b'') |
| 23 | USDZAR_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_em_ccy12m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | BCN12M_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | CCN12M_PX_LAST | b'double' | YES | bytearray(b'') |
| 4 | CHN12M_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | CLN12M_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | CZK12M_PX_LAST | b'double' | YES | bytearray(b'') |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 7 | HUF12M_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | IHN12M_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | ILS12M_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | IRN12M_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | KWN12M_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | MRN12M_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | MXN12M_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | NTN12M_PX_LAST | b'double' | YES | bytearray(b'') |
| 15 | PLN12M_PX_LAST | b'double' | YES | bytearray(b'') |
| 16 | PPN12M_PX_LAST | b'double' | YES | bytearray(b'') |
| 17 | RON12M_PX_LAST | b'double' | YES | bytearray(b'') |
| 18 | RUB12M_PX_LAST | b'double' | YES | bytearray(b'') |
| 19 | SGD12M_PX_LAST | b'double' | YES | bytearray(b'') |
| 20 | THB12M_PX_LAST | b'double' | YES | bytearray(b'') |
| 21 | TRY12M_PX_LAST | b'double' | YES | bytearray(b'') |
| 22 | ZAR12M_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_em_ccy1m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | BCN1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | CCN1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 4 | CHN1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | CLN1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | CZK1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 7 | HUF1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | IHN1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | ILS1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | IRN1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | KWN1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | MRN1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | MXN1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | NTN1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 15 | PLN1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 16 | PPN1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 17 | RON1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 18 | RUB1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 19 | SGD1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 20 | THB1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 21 | TRY1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 22 | ZAR1M_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_em_ccy6m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | BCN6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | CCN6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 4 | CHN6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | CLN6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | CZK6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 7 | HUF6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | IHN6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | ILS6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | IRN6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | KWN6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | MRN6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | MXN6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | NTN6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 15 | PLN6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 16 | PPN6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 17 | RON6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 18 | RUB6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 19 | SGD6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 20 | THB6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 21 | TRY6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 22 | ZAR6M_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_em_ccyusd () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | BRLUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | CLPUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 4 | CNHUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | COPUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | CZKUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 7 | HUFUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | IDRUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | ILSUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | INRUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | KRWUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | MXNUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | MYRUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | PHPUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 15 | PLNUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 16 | RONUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 17 | RUBUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 18 | SGDUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 19 | THBUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 20 | TRYUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 21 | TWDUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 22 | ZARUSD_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_em_cds () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | BRAZIL_CDS_USD_SR_5Y_D14_Corp_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | CHILE_CDS_USD_SR_5Y_D14_Corp_PX_LAST | b'double' | YES | bytearray(b'') |
| 4 | CHINAGOV_CDS_USD_SR_5Y_D14_Corp_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | COLOM_CDS_USD_SR_5Y_D14_Corp_PX_LAST | b'double' | YES | bytearray(b'') |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 6 | INDON_CDS_USD_SR_5Y_D14_Corp_PX_LAST | b'double' | YES | bytearray(b'') |
| 7 | KOREA_CDS_USD_SR_5Y_D14_Corp_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | MALAYS_CDS_USD_SR_5Y_D14_Corp_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | MEX_CDS_USD_SR_5Y_D14_Corp_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | PHILIP_CDS_USD_SR_5Y_D14_Corp_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | REPSOU_CDS_USD_SR_5Y_D14_Corp_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | RUSSIA_CDS_USD_SR_5Y_D14_Corp_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | THAI_CDS_USD_SR_5Y_D14_Corp_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | TURKEY_CDS_USD_SR_5Y_D14_Corp_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_em_eq () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | BET_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | BUX_PX_LAST | b'double' | YES | bytearray(b'') |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 4 | FBMKLCI_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | FSSTI_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | IBOV_PX_LAST | b'double' | YES | bytearray(b'') |
| 7 | IGBC_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | IPSA_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | JALSH_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | JCI_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | KOSPI_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | MEXBOL_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | NIFTY_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | PCOMP_PX_LAST | b'double' | YES | bytearray(b'') |
| 15 | PX_PX_LAST | b'double' | YES | bytearray(b'') |
| 16 | SET_PX_LAST | b'double' | YES | bytearray(b'') |
| 17 | SHCOMP_PX_LAST | b'double' | YES | bytearray(b'') |
| 18 | SPX_PX_LAST | b'double' | YES | bytearray(b'') |
| 19 | TA_25_PX_LAST | b'double' | YES | bytearray(b'') |
| 20 | TAMSCI_PX_LAST | b'double' | YES | bytearray(b'') |
| 21 | WIG_PX_LAST | b'double' | YES | bytearray(b'') |
| 22 | XU100_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_em_fs1y1m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | CCFS010A_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | CKFS010A_PX_LAST | b'double' | YES | bytearray(b'') |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 4 | HFFS010A_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | IRFS010A_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | KWFS010A_PX_LAST | b'double' | YES | bytearray(b'') |
| 7 | MPFS010A_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | PZFS010A_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | RRFS010A_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | SAFS010A_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | TYFS010A_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_em_fs3m1m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | CCFS0C0A_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | CKFS0C0A_PX_LAST | b'double' | YES | bytearray(b'') |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 4 | HFFS0C0A_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | IRFS0C0A_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | KWFS0C0A_PX_LAST | b'double' | YES | bytearray(b'') |
| 7 | MPFS0C0A_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | PZFS0C0A_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | RRFS0C0A_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | S0225FS_3M1M_BLC_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | SAFS0C0A_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | TYFS0C0A_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_em_gt10 () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 2 | GT10_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | GTBRL10Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 4 | GTCNY10Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | GTCOP10Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | GTCZK10Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 7 | GTHUF10Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | GTIDR10Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | GTILS10Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | GTINR10Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | GTMXN10Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | GTMYR10Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | GTPLN10Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | GTRON10Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 15 | GTRUB10Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 16 | GTSGD10Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 17 | GTTHB10Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 18 | GTZAR9Y_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_em_gt2 () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 2 | GT2_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | GTBRL2Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 4 | GTCLP2Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | GTCNY2Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | GTCOP2Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 7 | GTCZK2Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | GTHUF3Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | GTIDR2Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | GTILS2Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | GTINR2Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | GTKRW2Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | GTMXN2Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | GTPHP2Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 15 | GTPLN2Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 16 | GTRUB2Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 17 | GTSGD2Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 18 | GTTHB2Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 19 | GTTRY2Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 20 | GTTWD2Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 21 | GTZAR2Y_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_em_gt5 () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 2 | GT5_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | GTBRL5Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 4 | GTCLP5Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | GTCNY5Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | GTCOP6Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 7 | GTCZK5Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | GTHUF5Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | GTIDR5Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | GTILS5Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | GTINR5Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | GTKRW5Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | GTMXN5Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | GTMYR5Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 15 | GTPHP5Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 16 | GTPLN5Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 17 | GTRUB5Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 18 | GTSGD5Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 19 | GTTHB5Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 20 | GTTWD5Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 21 | GTZAR5Y_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_em_iv1m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 2 | USDBRLV1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | USDCLPV1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 4 | USDCNHV1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | USDCOPV1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | USDCZKV1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 7 | USDHUFV1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | USDIDRV1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | USDILSV1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | USDINRV1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | USDKRWV1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | USDMXNV1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | USDMYRV1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | USDPHPV1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 15 | USDPLNV1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 16 | USDRONV1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 17 | USDRUBV1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 18 | USDSGDV1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 19 | USDTHBV1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 20 | USDTRYV1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 21 | USDTWDV1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 22 | USDZARV1M_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_em_iv1y () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 2 | USDBRLV1Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | USDCLPV1Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 4 | USDCNHV1Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | USDCOPV1Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | USDCZKV1Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 7 | USDHUFV1Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | USDIDRV1Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | USDILSV1Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | USDINRV1Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | USDKRWV1Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | USDMXNV1Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | USDMYRV1Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | USDPHPV1Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 15 | USDPLNV1Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 16 | USDRONV1Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 17 | USDRUBV1Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 18 | USDSGDV1Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 19 | USDTHBV1Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 20 | USDTRYV1Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 21 | USDTWDV1Y_PX_LAST | b'double' | YES | bytearray(b'') |
| 22 | USDZARV1Y_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_em_iv6m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 2 | USDBRLV6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | USDCLPV6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 4 | USDCNHV6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | USDCOPV6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | USDCZKV6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 7 | USDHUFV6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | USDIDRV6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | USDILSV6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | USDINRV6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | USDKRWV6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | USDMXNV6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | USDMYRV6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | USDPHPV6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 15 | USDPLNV6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 16 | USDRONV6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 17 | USDRUBV6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 18 | USDSGDV6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 19 | USDTHBV6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 20 | USDTRYV6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 21 | USDTWDV6M_PX_LAST | b'double' | YES | bytearray(b'') |
| 22 | USDZARV6M_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_em_iy () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | BCNI1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | CHNI1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 4 | CLNI1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | CNHI1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | CZKI1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 7 | HUFI1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | IHNI1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | ILSI1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | IRNI1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | KWNI1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | MRNI1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | MXNI1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | NTNI1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 15 | PLNI1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 16 | PPNI1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 17 | RONI1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 18 | RUBI1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 19 | SGDI1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 20 | THBI1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 21 | TRYI1M_PX_LAST | b'double' | YES | bytearray(b'') |
| 22 | ZARI1M_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_em_jpmf () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 2 | JFRIBR_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | JFRICL_PX_LAST | b'double' | YES | bytearray(b'') |
| 4 | JFRICN_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | JFRICO_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | JFRICZ_PX_LAST | b'double' | YES | bytearray(b'') |
| 7 | JFRIHU_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | JFRIID_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | JFRIIL_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | JFRIIN_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | JFRIKR_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | JFRIMX_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | JFRIMY_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | JFRIPH_PX_LAST | b'double' | YES | bytearray(b'') |
| 15 | JFRIPL_PX_LAST | b'double' | YES | bytearray(b'') |
| 16 | JFRIRO__PX_LAST | b'double' | YES | bytearray(b'') |
| 17 | JFRIRU_PX_LAST | b'double' | YES | bytearray(b'') |
| 18 | JFRISG_PX_LAST | b'double' | YES | bytearray(b'') |
| 19 | JFRITH_PX_LAST | b'double' | YES | bytearray(b'') |
| 20 | JFRITR_PX_LAST | b'double' | YES | bytearray(b'') |
| 21 | JFRITW_PX_LAST | b'double' | YES | bytearray(b'') |
| 22 | JFRIUS_PX_LAST | b'double' | YES | bytearray(b'') |
| 23 | JFRIZA_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_em_on () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | BOFXON_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | BUBORON_PX_LAST | b'double' | YES | bytearray(b'') |
| 4 | BUBRON_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | BZSELICA_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | CHOVCHOV_PX_LAST | b'double' | YES | bytearray(b'') |
| 7 | CKDR2T_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | COOVIBR_PX_LAST | b'double' | YES | bytearray(b'') |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 9 | FEDL01_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | HICNHON_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | IN00ON_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | JIINON_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | KWCR1T_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | MRDR1T_PX_LAST | b'double' | YES | bytearray(b'') |
| 15 | MXONBR_PX_LAST | b'double' | YES | bytearray(b'') |
| 16 | PREFON_PX_LAST | b'double' | YES | bytearray(b'') |
| 17 | PRIMTA_PX_LAST | b'double' | YES | bytearray(b'') |
| 18 | RUONIA_PX_LAST | b'double' | YES | bytearray(b'') |
| 19 | SARPRT_PX_LAST | b'double' | YES | bytearray(b'') |
| 20 | SDDR1T_PX_LAST | b'double' | YES | bytearray(b'') |
| 21 | TELBORON_PX_LAST | b'double' | YES | bytearray(b'') |
| 22 | TRLIBON_PX_LAST | b'double' | YES | bytearray(b'') |
| 23 | WIBOON_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_em_rr1m () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 2 | USDBRL25R3M_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | USDCLP25R3M_PX_LAST | b'double' | YES | bytearray(b'') |
| 4 | USDCNH25R3M_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | USDCOP25R3M_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | USDCZK25R3M_PX_LAST | b'double' | YES | bytearray(b'') |
| 7 | USDHUF25R3M_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | USDIDR25R3M_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | USDILS25R3M_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | USDINR25R3M_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | USDKRW25R3M_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | USDMXN25R3M_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | USDMYR25R3M_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | USDPHP25R3M_PX_LAST | b'double' | YES | bytearray(b'') |
| 15 | USDPLN25R3M_PX_LAST | b'double' | YES | bytearray(b'') |
| 16 | USDRON25R3M_PX_LAST | b'double' | YES | bytearray(b'') |
| 17 | USDRUB25R3M_PX_LAST | b'double' | YES | bytearray(b'') |
| 18 | USDSGD25R3M_PX_LAST | b'double' | YES | bytearray(b'') |
| 19 | USDTHB25R3M_PX_LAST | b'double' | YES | bytearray(b'') |
| 20 | USDTRY25R3M_PX_LAST | b'double' | YES | bytearray(b'') |
| 21 | USDTWD25R3M_PX_LAST | b'double' | YES | bytearray(b'') |
| 22 | USDZAR25R3M_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_em_tickers () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | value | b'varchar(255)' | YES | bytearray(b'') |
| 1 | Var1 | b'varchar(255)' | YES | bytearray(b'') |
| 2 | Var2 | b'varchar(255)' | YES | bytearray(b'') |



### s09_em_twi () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 2 | MSCEBRTW_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | MSCECLTW_PX_LAST | b'double' | YES | bytearray(b'') |
| 4 | MSCECNTW_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | MSCECOTW_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | MSCECZTW_PX_LAST | b'double' | YES | bytearray(b'') |
| 7 | MSCEHUTW_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | MSCEIDTW_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | MSCEILTW_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | MSCEINTW_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | MSCEKRTW_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | MSCEMXTW_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | MSCEMYTW_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | MSCEPLTW_PX_LAST | b'double' | YES | bytearray(b'') |
| 15 | MSCERUTW_PX_LAST | b'double' | YES | bytearray(b'') |
| 16 | MSCESGTW_PX_LAST | b'double' | YES | bytearray(b'') |
| 17 | MSCETHTW_PX_LAST | b'double' | YES | bytearray(b'') |
| 18 | MSCETRTW_PX_LAST | b'double' | YES | bytearray(b'') |
| 19 | MSCETWTW_PX_LAST | b'double' | YES | bytearray(b'') |
| 20 | MSCEUSTW_PX_LAST | b'double' | YES | bytearray(b'') |
| 21 | MSCEZATW_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_em_vola () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | CL1_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | CO1_PX_LAST | b'double' | YES | bytearray(b'') |
| 4 | CRB_CMDT_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | CRB_FOOD_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | CRB_METL_PX_LAST | b'double' | YES | bytearray(b'') |
| 7 | CRB_RIND_PX_LAST | b'double' | YES | bytearray(b'') |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 9 | FF12_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | FF1_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | HG1_COMB_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | L_12_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | L_1_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | LMCADS03_LME_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | VIX_PX_LAST | b'double' | YES | bytearray(b'') |
| 15 | VV2TX_PX_LAST | b'double' | YES | bytearray(b'') |
| 16 | VXO_PX_LAST | b'double' | YES | bytearray(b'') |
| 17 | XAG_PX_LAST | b'double' | YES | bytearray(b'') |
| 18 | XAU_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_fut_memberrankbyoption () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | EndDate | b'datetime' | NO | bytearray(b'') |
| 3 | OptionCode | b'int(11)' | YES | bytearray(b'') |
| 8 | PosLTop10 | b'decimal(18,4)' | YES | bytearray(b'') |
| 9 | PosLTop20 | b'decimal(18,4)' | YES | bytearray(b'') |
| 7 | PosLTop5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 11 | PosSTop10 | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | PosSTop20 | b'decimal(18,4)' | YES | bytearray(b'') |
| 10 | PosSTop5 | b'decimal(18,4)' | YES | bytearray(b'') |
| 2 | UploadTime | b'datetime' | NO | bytearray(b'') |
| 5 | VolTop10 | b'decimal(18,4)' | YES | bytearray(b'') |
| 6 | VolTop20 | b'decimal(18,4)' | YES | bytearray(b'') |
| 4 | VolTop5 | b'decimal(18,4)' | YES | bytearray(b'') |



### s09_fut_res () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 14 | ClosePrice | b'varchar(255)' | YES | bytearray(b'') |
| 9 | Cont1 | b'varchar(255)' | YES | bytearray(b'') |
| 2 | EndDate | b'varchar(255)' | YES | bytearray(b'') |
| 3 | Exchange | b'varchar(255)' | YES | bytearray(b'') |
| 1 | f1 | b'varchar(255)' | YES | bytearray(b'') |
| 12 | HighPrice | b'varchar(255)' | YES | bytearray(b'') |
| 13 | LowPrice | b'varchar(255)' | YES | bytearray(b'') |
| 6 | M_SettlementDate | b'varchar(255)' | YES | bytearray(b'') |
| 5 | Main | b'varchar(255)' | YES | bytearray(b'') |
| 17 | OpenInterest | b'varchar(255)' | YES | bytearray(b'') |
| 11 | OpenPrice | b'varchar(255)' | YES | bytearray(b'') |
| 4 | OptionCode | b'varchar(255)' | YES | bytearray(b'') |
| 10 | PrevSettlePrice | b'varchar(255)' | YES | bytearray(b'') |
| 15 | SettlePrice | b'varchar(255)' | YES | bytearray(b'') |
| 8 | SM_SettlementDate | b'varchar(255)' | YES | bytearray(b'') |
| 7 | SMain | b'varchar(255)' | YES | bytearray(b'') |
| 18 | Turnover | b'varchar(255)' | YES | bytearray(b'') |
| 16 | Volume | b'varchar(255)' | YES | bytearray(b'') |



### s09_fx () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 27 | AUDUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 32 | datetime | b'date' | YES | bytearray(b'') |
| 2 | DXY_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | EURUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | GBPUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 1 | id | b'double' | YES | bytearray(b'') |
| 4 | NZDUSD_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | USDBRL_PX_LAST | b'double' | YES | bytearray(b'') |
| 7 | USDCAD_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | USDCHF_PX_LAST | b'double' | YES | bytearray(b'') |
| 20 | USDCLP_PX_LAST | b'double' | YES | bytearray(b'') |
| 30 | USDCNY_PX_LAST | b'double' | YES | bytearray(b'') |
| 25 | USDCOP_PX_LAST | b'double' | YES | bytearray(b'') |
| 29 | USDCZK_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | USDHUF_PX_LAST | b'double' | YES | bytearray(b'') |
| 31 | USDIDR_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | USDILS_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | USDINR_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | USDJPY_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | USDKRW_PX_LAST | b'double' | YES | bytearray(b'') |
| 17 | USDMXN_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | USDMYR_PX_LAST | b'double' | YES | bytearray(b'') |
| 23 | USDNOK_PX_LAST | b'double' | YES | bytearray(b'') |
| 15 | USDPHP_PX_LAST | b'double' | YES | bytearray(b'') |
| 16 | USDPLN_PX_LAST | b'double' | YES | bytearray(b'') |
| 21 | USDRUB_PX_LAST | b'double' | YES | bytearray(b'') |
| 19 | USDSEK_PX_LAST | b'double' | YES | bytearray(b'') |
| 18 | USDSGD_PX_LAST | b'double' | YES | bytearray(b'') |
| 22 | USDTHB_PX_LAST | b'double' | YES | bytearray(b'') |
| 24 | USDTRY_PX_LAST | b'double' | YES | bytearray(b'') |
| 26 | USDTWD_PX_LAST | b'double' | YES | bytearray(b'') |
| 28 | USDZAR_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_fx_tickers () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | tickers | b'varchar(255)' | YES | bytearray(b'') |



### s09_img_holdid () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | ACCT_ID | b'varchar(20)' | YES | bytearray(b'\xe7\xbb\x93\xe7\xae\x97\xe5\x8d\x95\xe8\xb5\x84\xe9\x87\x91\xe8\xb4\xa6\xe6\x88\xb7') |
| 6 | Email | b'varchar(255)' | YES | bytearray(b'\xe5\x8f\x91\xe4\xbb\xb6\xe4\xba\xba\xe9\x82\xae\xe7\xae\xb1') |
| 1 | IMG_ACCT | b'varchar(50)' | YES | bytearray(b'Imagine\xe7\xb3\xbb\xe7\xbb\x9f\xe9\x87\x8c\xe7\x9a\x84\xe8\xb4\xa6\xe6\x88\xb7') |
| 2 | IMG_CUST | b'varchar(20)' | YES | bytearray(b'Imagine\xe7\xb3\xbb\xe7\xbb\x9f\xe9\x87\x8c\xe7\x9a\x84Custodian') |
| 3 | IMG_HOLDID | b'int(20)' | YES | bytearray(b'Imagine Holding ID') |
| 5 | IMG_LE | b'varchar(20)' | YES | bytearray(b'Imagine\xe5\x9f\xba\xe9\x87\x91') |



### s09_img_mapping () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | Imagine | b'varchar(50)' | YES | bytearray(b'') |
| 2 | WCode | b'varchar(50)' | YES | bytearray(b'') |
| 1 | WExch | b'varchar(50)' | YES | bytearray(b'') |



### s09_jy_volbyoptioncode (合约库存排名数据表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | contractcode | b'varchar(10)' | YES | bytearray(b'\xe5\x90\x88\xe7\xba\xa6\xe4\xbb\xa3\xe7\xa0\x81') |
| 1 | enddate | b'datetime' | YES | bytearray(b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f') |
| 2 | exchangecode | b'int(11)' | YES | bytearray(b'\xe4\xba\xa4\xe6\x98\x93\xe6\x89\x80') |
| 5 | indicatorCode | b'int(11)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe4\xbb\xa3\xe7\xa0\x81') |
| 6 | indicatorName | b'varchar(50)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe5\x90\x8d\xe7\xa7\xb0') |
| 7 | indicatorVolume | b'decimal(18,4)' | YES | bytearray(b'\xe6\x8c\x87\xe6\xa0\x87\xe6\x95\xb0\xe9\x87\x8f(\xe6\x89\x8b)') |
| 8 | inserttime | b'datetime' | YES | bytearray(b'\xe6\x8f\x92\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4') |
| 3 | OptionCode | b'int(11)' | YES | bytearray(b'\xe5\x93\x81\xe7\xa7\x8d\xe4\xbb\xa3\xe7\xa0\x81') |
| 9 | UpdateTime | b'datetime' | YES | bytearray(b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4') |



### s09_lev_calc () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | EXCHCODE | b'varchar(50)' | YES | bytearray(b'') |
| 2 | PX | b'float' | YES | bytearray(b'') |



### s09_lev_calc_os () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | EXCHCODE | b'varchar(50)' | YES | bytearray(b'') |
| 2 | PX | b'float' | YES | bytearray(b'') |



### s09_misc () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Ticker | b'varchar(255)' | YES | bytearray(b'') |



### s09_misc2 () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | Date | b'varchar(255)' | YES | bytearray(b'') |
| 3 | Fields | b'varchar(255)' | YES | bytearray(b'') |
| 1 | Ticker | b'varchar(255)' | YES | bytearray(b'') |
| 4 | Values | b'double' | YES | bytearray(b'') |



### s09_otc_id () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | Cost | b'decimal(10,3)' | YES | bytearray(b'\xe5\x85\xa5\xe5\x9c\xba\xe6\xa0\x87\xe7\x9a\x84\xe4\xbb\xb7\xef\xbc\x88\xe4\xb8\x93\xe4\xbe\x9bHTCC\xef\xbc\x89') |
| 1 | DEAL_ID | b'varchar(100)' | YES | bytearray(b'\xe5\xaf\xb9\xe6\x89\x8b\xe7\xbb\x99\xe7\x9a\x84ID') |
| 2 | IMG_ID | b'varchar(100)' | YES | bytearray(b'Imagine\xe7\xb3\xbb\xe7\xbb\x9f\xe9\x87\x8c\xe7\x9a\x84Holding ID') |
| 3 | IMG_Secu | b'varchar(100)' | YES | bytearray(b'Imagine\xe7\xb3\xbb\xe7\xbb\x9f\xe9\x87\x8c\xe7\x9a\x84\xe6\xa0\x87\xe7\x9a\x84') |
| 4 | TradeDt | b'timestamp(6)' | YES | bytearray(b'\xe6\x88\x90\xe4\xba\xa4\xe6\x97\xa5\xef\xbc\x88\xe4\xb8\x93\xe4\xbe\x9bHTCC\xef\xbc\x89') |



### s09_portfolio () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 9 | AvgCost | b'decimal(18,6)' | YES | bytearray(b'') |
| 6 | BBTicker | b'varchar(50)' | YES | bytearray(b'') |
| 10 | Commission | b'decimal(18,6)' | YES | bytearray(b'') |
| 12 | ContrSiz | b'int(50)' | YES | bytearray(b'') |
| 2 | Curr | b'varchar(10)' | YES | bytearray(b'') |
| 15 | Direction | b'int(5)' | YES | bytearray(b'') |
| 5 | exch_usym | b'varchar(30)' | YES | bytearray(b'') |
| 14 | exchangecode | b'varchar(30)' | YES | bytearray(b'') |
| 4 | ExchCode | b'varchar(30)' | YES | bytearray(b'') |
| 11 | holdPortfXrate | b'decimal(18,6)' | YES | bytearray(b'') |
| 8 | Qty | b'decimal(18,6)' | YES | bytearray(b'') |
| 3 | secu | b'varchar(30)' | YES | bytearray(b'') |
| 13 | SubAcc | b'varchar(50)' | YES | bytearray(b'') |
| 1 | tradingday | b'datetime' | YES | bytearray(b'') |
| 7 | usym | b'varchar(50)' | YES | bytearray(b'') |



### s09_prod () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 8 | CValue | b'decimal(18,5)' | NO | bytearray(b'') |
| 10 | DailyReturn | b'decimal(18,6)' | YES | bytearray(b'') |
| 11 | Dropdown | b'decimal(18,6)' | YES | bytearray(b'') |
| 1 | id | b'int(11)' | NO | bytearray(b'') |
| 13 | IsDvdYear | b'int(11)' | YES | bytearray(b'') |
| 9 | MaxValue | b'decimal(18,5)' | NO | bytearray(b'') |
| 5 | ProdAUM | b'decimal(18,4)' | YES | bytearray(b'') |
| 3 | ProdID | b'varchar(20)' | NO | bytearray(b'') |
| 4 | ProdName | b'varchar(200)' | NO | bytearray(b'') |
| 6 | ProdShare | b'decimal(18,4)' | YES | bytearray(b'') |
| 12 | UpdateTime | b'datetime(6)' | NO | bytearray(b'') |
| 2 | ValuationDate | b'datetime(6)' | NO | bytearray(b'') |
| 7 | Value | b'decimal(18,5)' | NO | bytearray(b'') |



### s09_prod_risk_param () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 8 | FutureGrossLev | b'varchar(255)' | YES | bytearray(b'') |
| 9 | FutureNetLev | b'varchar(255)' | YES | bytearray(b'') |
| 5 | NAVdown | b'varchar(255)' | YES | bytearray(b'') |
| 4 | NAVup | b'varchar(255)' | YES | bytearray(b'') |
| 2 | ProdID | b'varchar(255)' | YES | bytearray(b'') |
| 1 | ProdName | b'varchar(255)' | YES | bytearray(b'') |
| 3 | RuleType | b'varchar(255)' | YES | bytearray(b'') |
| 10 | SingleFutureLev | b'varchar(255)' | YES | bytearray(b'') |
| 7 | SingleStockLev | b'varchar(255)' | YES | bytearray(b'') |
| 6 | StockLev | b'varchar(255)' | YES | bytearray(b'') |



### s09_prod_warning_prodmap (产品预警对应表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | CloseOutline | b'decimal(19,2)' | YES | bytearray(b'\xe5\xb9\xb3\xe4\xbb\x93\xe7\xba\xbf') |
| 5 | ID | b'int(11)' | YES | bytearray(b'\xe8\x87\xaa\xe5\xa2\x9eID') |
| 1 | ProdId | b'varchar(50)' | YES | bytearray(b'\xe4\xba\xa7\xe5\x93\x81\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | ProdName | b'varchar(50)' | YES | bytearray(b'\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0') |
| 3 | WarningLine | b'decimal(19,2)' | YES | bytearray(b'\xe9\xa2\x84\xe8\xad\xa6\xe7\xba\xbf') |



### s09_risk_df () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | AD1_PX_LAST | b'double' | YES | bytearray(b'') |
| 3 | BIT1_PX_LAST | b'double' | YES | bytearray(b'') |
| 4 | BP1_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | CD1_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | CL1_PX_LAST | b'double' | YES | bytearray(b'') |
| 7 | CO1_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | CU1_PX_LAST | b'double' | YES | bytearray(b'') |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 9 | DM1_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | DX1_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | EC1_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | ES1_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | GC1_PX_LAST | b'double' | YES | bytearray(b'') |
| 14 | GX1_PX_LAST | b'double' | YES | bytearray(b'') |
| 15 | HG1_PX_LAST | b'double' | YES | bytearray(b'') |
| 16 | HI1_PX_LAST | b'double' | YES | bytearray(b'') |
| 17 | IOE1_PX_LAST | b'double' | YES | bytearray(b'') |
| 18 | JY1_PX_LAST | b'double' | YES | bytearray(b'') |
| 19 | KEE1_PX_LAST | b'double' | YES | bytearray(b'') |
| 20 | LMCADS03_PX_LAST | b'double' | YES | bytearray(b'') |
| 21 | LMZSDS03_PX_LAST | b'double' | YES | bytearray(b'') |
| 22 | NI1_PX_LAST | b'double' | YES | bytearray(b'') |
| 23 | NQ1_PX_LAST | b'double' | YES | bytearray(b'') |
| 24 | NV1_PX_LAST | b'double' | YES | bytearray(b'') |
| 25 | PE1_PX_LAST | b'double' | YES | bytearray(b'') |
| 26 | RBT1_PX_LAST | b'double' | YES | bytearray(b'') |
| 27 | SI1_PX_LAST | b'double' | YES | bytearray(b'') |
| 28 | UX1_PX_LAST | b'double' | YES | bytearray(b'') |
| 29 | VG1_PX_LAST | b'double' | YES | bytearray(b'') |
| 30 | VIX_PX_LAST | b'double' | YES | bytearray(b'') |
| 31 | Z_1_PX_LAST | b'double' | YES | bytearray(b'') |
| 32 | ZNA1_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_rmm () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | Date | b'varchar(255)' | YES | bytearray(b'') |
| 3 | Fields | b'varchar(255)' | YES | bytearray(b'') |
| 1 | Ticker | b'varchar(255)' | YES | bytearray(b'') |
| 4 | Values | b'double' | YES | bytearray(b'') |



### s09_rmt () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Ticker | b'varchar(255)' | YES | bytearray(b'') |



### s09_rsk_fx_data () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | datetime | b'date' | NO | bytearray(b'') |
| 6 | PX_CLOSE | b'double' | YES | bytearray(b'') |
| 4 | PX_HIGH | b'double' | YES | bytearray(b'') |
| 5 | PX_LOW | b'double' | YES | bytearray(b'') |
| 3 | PX_OPEN | b'double' | YES | bytearray(b'') |
| 7 | PX_SETTLE | b'double' | YES | bytearray(b'') |
| 1 | Ticker | b'varchar(255)' | YES | bytearray(b'') |



### s09_rsk_img () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | datetime | b'datetime(6)' | YES | bytearray(b'') |
| 5 | id | b'double' | YES | bytearray(b'') |
| 3 | price | b'double' | YES | bytearray(b'') |
| 1 | symbol | b'varchar(255)' | YES | bytearray(b'') |
| 2 | usym | b'varchar(255)' | YES | bytearray(b'') |



### s09_rsk_img2 () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | datetime | b'text' | YES | bytearray(b'') |
| 6 | id | b'double' | YES | bytearray(b'') |
| 4 | price | b'double' | YES | bytearray(b'') |
| 1 | row_names | b'text' | YES | bytearray(b'') |
| 2 | symbol | b'text' | YES | bytearray(b'') |
| 3 | usym | b'text' | YES | bytearray(b'') |



### s09_rsk_img_usym_ts () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | datetime | b'date' | NO | bytearray(b'') |
| 4 | HIGH | b'double' | YES | bytearray(b'') |
| 5 | LOW | b'double' | YES | bytearray(b'') |
| 3 | OPEN | b'double' | YES | bytearray(b'') |
| 8 | OPEN_INT | b'int(11)' | YES | bytearray(b'') |
| 10 | PX_ASK | b'double' | YES | bytearray(b'') |
| 9 | PX_BID | b'double' | YES | bytearray(b'') |
| 6 | PX_LAST | b'double' | YES | bytearray(b'') |
| 1 | Ticker | b'varchar(255)' | YES | bytearray(b'') |
| 7 | VOLUME | b'double' | YES | bytearray(b'') |



### s09_rsk_tickers () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | tickers | b'varchar(255)' | YES | bytearray(b'') |
| 2 | u1 | b'varchar(255)' | YES | bytearray(b'') |



### s09_rsk_usym_bbg_map () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | BBticker | b'varchar(255)' | YES | bytearray(b'') |
| 1 | Usym | b'varchar(255)' | YES | bytearray(b'') |
| 3 | Usym2 | b'varchar(255)' | YES | bytearray(b'') |



### s09_skm () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | Date | b'varchar(255)' | YES | bytearray(b'') |
| 3 | Fields | b'varchar(255)' | YES | bytearray(b'') |
| 1 | Ticker | b'varchar(255)' | YES | bytearray(b'') |
| 4 | Values | b'double' | YES | bytearray(b'') |



### s09_skt () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Ticker | b'varchar(255)' | YES | bytearray(b'') |



### s09_strat_mapping () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 8 | ASST | b'varchar(50)' | YES | bytearray(b'') |
| 9 | ASSTCLASS | b'varchar(50)' | YES | bytearray(b'') |
| 3 | BBGTICKER | b'varchar(50)' | YES | bytearray(b'') |
| 2 | DSYM | b'varchar(50)' | YES | bytearray(b'') |
| 1 | SECURI | b'varchar(50)' | YES | bytearray(b'') |
| 6 | STRATEGY | b'varchar(50)' | YES | bytearray(b'') |
| 7 | TEAM | b'varchar(50)' | YES | bytearray(b'') |
| 5 | TYPE | b'varchar(50)' | YES | bytearray(b'') |
| 4 | WINDCODE | b'varchar(50)' | YES | bytearray(b'') |



### s09_sysdiagrams () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | definition | b'longblob' | YES | bytearray(b'') |
| 3 | diagram_id | b'int(11)' | NO | bytearray(b'') |
| 1 | name | b'varchar(160)' | NO | bytearray(b'') |
| 2 | principal_id | b'int(11)' | NO | bytearray(b'') |
| 4 | version | b'int(11)' | YES | bytearray(b'') |



### s09_temp_hist () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | Date | b'varchar(50)' | YES | bytearray(b'') |
| 3 | Field | b'varchar(50)' | YES | bytearray(b'') |
| 1 | Ticker | b'varchar(50)' | YES | bytearray(b'') |
| 4 | Value | b'double' | YES | bytearray(b'') |



### s09_test () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | datetime | b'date' | NO | bytearray(b'') |
| 3 | HIGH | b'double' | YES | bytearray(b'') |
| 4 | LOW | b'double' | YES | bytearray(b'') |
| 2 | OPEN | b'double' | YES | bytearray(b'') |
| 7 | OPEN_INT | b'int(11)' | YES | bytearray(b'') |
| 9 | PX_ASK | b'double' | YES | bytearray(b'') |
| 8 | PX_BID | b'double' | YES | bytearray(b'') |
| 5 | PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | VOLUME | b'double' | YES | bytearray(b'') |



### s09_test2 () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | BB Ticker | b'text' | YES | bytearray(b'') |
| 7 | Curr | b'text' | YES | bytearray(b'') |
| 6 | Exch | b'text' | YES | bytearray(b'') |
| 2 | Holding ID | b'text' | YES | bytearray(b'') |
| 9 | Mkt | b'text' | YES | bytearray(b'') |
| 8 | Quantity | b'text' | YES | bytearray(b'') |
| 1 | row_names | b'text' | YES | bytearray(b'') |
| 3 | Security | b'text' | YES | bytearray(b'') |
| 4 | SM Dsym | b'text' | YES | bytearray(b'') |
| 11 | SY QDCode | b'text' | YES | bytearray(b'') |
| 12 | SY QDTicker | b'text' | YES | bytearray(b'') |
| 10 | SY Security | b'text' | YES | bytearray(b'') |



### s09_test99 () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Column 1 | b'int(11)' | YES | bytearray(b'') |
| 2 | Column 2 | b'int(11)' | YES | bytearray(b'') |
| 3 | Column 3 | b'int(11)' | YES | bytearray(b'') |



### s09_test_create () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | C1 | b'int(11)' | YES | bytearray(b'') |



### s09_test_update () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | Date | b'varchar(255)' | YES | bytearray(b'') |
| 3 | Field | b'varchar(255)' | YES | bytearray(b'') |
| 2 | Ticker | b'varchar(255)' | YES | bytearray(b'') |
| 4 | Value | b'double' | YES | bytearray(b'') |



### s09_ticker_mapping_cn () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | IMGCODE | b'varchar(50)' | YES | bytearray(b'') |
| 4 | IMGEXCH | b'varchar(50)' | YES | bytearray(b'') |
| 2 | WCODE | b'varchar(50)' | YES | bytearray(b'') |
| 1 | WEXCH | b'varchar(50)' | YES | bytearray(b'') |



### s09_usmacro () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | CPI XCHG_PX_LAST | b'double' | YES | bytearray(b'') |
| 2 | datetime | b'date' | YES | bytearray(b'') |
| 1 | id | b'double' | YES | bytearray(b'') |
| 16 | INDX_GENERAL_EST_PE_INDX_GENERAL_EST_PE | b'double' | YES | bytearray(b'') |
| 15 | INDX_GENERAL_PE_RATIO_INDX_GENERAL_PE_RATIO | b'double' | YES | bytearray(b'') |
| 14 | IP CHNG_PX_LAST | b'double' | YES | bytearray(b'') |
| 11 | LF98OAS_PX_LAST | b'double' | YES | bytearray(b'') |
| 10 | LUACOAS_PX_LAST | b'double' | YES | bytearray(b'') |
| 7 | OEUSDHAO_PX_LAST | b'double' | YES | bytearray(b'') |
| 5 | OEUSLCAC_PX_LAST | b'double' | YES | bytearray(b'') |
| 6 | SPX_PX_LAST | b'double' | YES | bytearray(b'') |
| 13 | USGG10YR_PX_LAST | b'double' | YES | bytearray(b'') |
| 12 | USGG2YR_PX_LAST | b'double' | YES | bytearray(b'') |
| 4 | USURTOT_PX_LAST | b'double' | YES | bytearray(b'') |
| 8 | VIX_PX_LAST | b'double' | YES | bytearray(b'') |
| 9 | VXO_PX_LAST | b'double' | YES | bytearray(b'') |



### s09_usmacro_tickers () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | tickers | b'varchar(255)' | YES | bytearray(b'') |



### s09_xdh_lev () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | EXCHCODE | b'varchar(50)' | YES | bytearray(b'') |
| 2 | PX | b'decimal(10,0)' | YES | bytearray(b'') |



### zold_bs_enddate () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | enddate | b'datetime' | NO | bytearray(b'') |



### zold_bs_fin () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | ChiName | b'varchar(200)' | YES | bytearray(b'\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d\xe7\xa7\xb0') |
| 2 | ChiNameAbbr | b'varchar(100)' | YES | bytearray(b'\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d\xe7\xa7\xb0\xe7\xbc\xa9\xe5\x86\x99') |
| 4 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 3 | FirstIndustryName | b'varchar(100)' | YES | bytearray(b'\xe4\xba\x8c\xe7\xba\xa7\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0') |



### zold_bs_lc_incomestatementall () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | AdministrationExpense | b'decimal(21,4)' | YES | bytearray(b'') |
| 1 | id | b'bigint(20)' | NO | bytearray(b'ID') |



### zold_bs_threeyear () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | EndDate | b'datetime' | YES | bytearray(b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f') |
| 5 | ListedDate | b'datetime' | YES | bytearray(b'\xe4\xb8\x8a\xe5\xb8\x82\xe6\x97\xa5\xe6\x9c\x9f') |
| 3 | ROE | b'decimal(19,4)' | YES | bytearray(b'ROE\xef\xbc\x88\xe5\xbd\x92\xe6\xaf\x8d\xe6\x9d\x83\xe7\x9b\x8a\xef\xbc\x89') |
| 4 | SecondIndustryName | b'varchar(100)' | YES | bytearray(b'\xe5\xaf\xb9\xe5\xba\x94\xe4\xba\x8c\xe7\xba\xa7\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0') |



### zold_bs_twoyear () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | CompanyCode | b'int(11)' | YES | bytearray(b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81') |
| 2 | EndDate | b'datetime' | YES | bytearray(b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f') |
| 5 | ListedDate | b'datetime' | YES | bytearray(b'\xe4\xb8\x8a\xe5\xb8\x82\xe6\x97\xa5\xe6\x9c\x9f') |
| 3 | ROE | b'decimal(19,4)' | YES | bytearray(b'ROE\xef\xbc\x88\xe5\xbd\x92\xe6\xaf\x8d\xe6\x9d\x83\xe7\x9b\x8a\xef\xbc\x89') |
| 4 | SecondIndustryName | b'varchar(100)' | YES | bytearray(b'\xe5\xaf\xb9\xe5\xba\x94\xe4\xba\x8c\xe7\xba\xa7\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0') |
