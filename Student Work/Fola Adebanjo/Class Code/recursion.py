Functioinm listSukm(list) // recursive
	IF list.length == 0 THEN
		return 0
	ELSE
		RETURN list[0] + listSum(list[1:])
	END IF
END FUNCTIION