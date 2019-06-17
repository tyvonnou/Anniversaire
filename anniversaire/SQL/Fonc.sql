--
-- Fonctions
--
DELIMITER //
CREATE FUNCTION `AGE` (`naissance` DATE) RETURNS INT(11) BEGIN
    DECLARE age INT;
 
    IF (DAY(current_date) >= DAY(naissance) AND MONTH(current_date) >= MONTH(naissance)) OR (MONTH(current_date) > MONTH(naissance)) THEN
        set age = YEAR(current_date) - YEAR(naissance);
    ELSE
        set age = YEAR(current_date) - YEAR(naissance) - 1;
    END IF;
 
 RETURN (age);
END
//
DELIMITER //
CREATE FUNCTION `jrest` (`naissance` DATE) RETURNS INT(11) BEGIN
	IF (dayofyear(naissance) - dayofyear(NOW())) > 0 THEN
		RETURN (dayofyear(naissance) - dayofyear(NOW()));
    END IF;
    
    RETURN dayofyear(naissance) + 365 - dayofyear(NOW());
END
//
DELIMITER ;
