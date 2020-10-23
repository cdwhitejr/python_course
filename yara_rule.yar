rule upx_test

{
	strings:
		$a = "UPX"
		$b = "GetMo"
	condition:
		$a and $b
}
