DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
    IN pf_name VARCHAR(50),
    IN pl_name VARCHAR(50),
    IN p_email VARCHAR(50),
    IN p_phone VARCHAR(14),
    IN p_password VARCHAR(30)
)
BEGIN
    if ( select exists (select 1 from tbl_user where phone = p_phone) ) THEN
     
        select 'Phone Exists !!';
     
    ELSE
     
        insert into tbl_user
        (
            f_name,
	    l_name,
	    email,
            phone,
            password
        )
        values
        (
            pf_name,
	    pl_name,
            p_email,
	    p_phone,
            p_password
        );
     
    END IF;
END$$
DELIMITER ;
