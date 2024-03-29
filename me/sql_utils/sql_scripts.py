CreateTableScript={
    "ROLE":"CREATE TABLE ROLE ( ID INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(10));",
    "CRM":"CREATE TABLE CRM ( ID INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(255), DESCRIPTION VARCHAR(1000), WEBSITE VARCHAR(255));",
    "USER":"CREATE TABLE USERS( ID VARCHAR(100) PRIMARY KEY, USERNAME VARCHAR(255) UNIQUE, ROLE_ID INT DEFAULT 1, CRM_ID INT DEFAULT 1, EMAIL VARCHAR(500), FIRSTNAME VARCHAR(255), LASTNAME VARCHAR(255), PHONENUMBER VARCHAR(255), MOBILEPHONENUMBER VARCHAR(255), ACTIVATED TINYINT(1) DEFAULT 0, CREATEDDATE DATETIME DEFAULT CURRENT_TIMESTAMP, UPDATEDDATE DATETIME DEFAULT CURRENT_TIMESTAMP, CONSTRAINT FK_USERROLE FOREIGN KEY (ROLE_ID) REFERENCES ROLE(ID), CONSTRAINT FK_CRMROLE FOREIGN KEY (CRM_ID) REFERENCES CRM(ID) );",
    "SERVICE":"CREATE TABLE SERVICE ( ID INT AUTO_INCREMENT PRIMARY KEY, USER_ID VARCHAR(100) NOT NULL, CRM_ID INT NOT NULL, TITLE VARCHAR(255), DESCRIPTION VARCHAR(1000), CONSTRAINT FK_CRMSERVICE FOREIGN KEY (CRM_ID) REFERENCES CRM(ID), CONSTRAINT FK_USERSERVICE FOREIGN KEY (USER_ID) REFERENCES USERS(ID) );",
    "VENUES":"CREATE TABLE VENUES ( ID INT AUTO_INCREMENT PRIMARY KEY, CRM_ID INT NOT NULL, NAME VARCHAR(255), DESCRIPTION VARCHAR(1000), PHONE_NUMBER VARCHAR(20), LATITUDE DOUBLE, LONGITUDE DOUBLE, ADDRESS VARCHAR(500), SUBURB VARCHAR(500), CITY VARCHAR(500), STATE VARCHAR(500), COUNTRY VARCHAR(500), POST_CODE VARCHAR(500), CONSTRAINT FK_CRMVENUE FOREIGN KEY (CRM_ID) REFERENCES CRM(ID));",
    "VENUES_OPEN_HOUR":"CREATE TABLE VENUES_OPEN_HOUR ( ID INT AUTO_INCREMENT PRIMARY KEY, VENUE_ID INT NOT NULL, DAY VARCHAR(3), OPEN_TIME TIME, CLOSE_TIME TIME, CONSTRAINT FK_VENUE_OPENHOUR FOREIGN KEY (VENUE_ID) REFERENCES VENUES(ID));",
    "TAG": "CREATE TABLE TAG ( ID INT AUTO_INCREMENT PRIMARY KEY, CRM_ID INT NOT NULL, NAME VARCHAR(255), CONSTRAINT FK_CRMTAG FOREIGN KEY (CRM_ID) REFERENCES CRM(ID));",
    "SERVICE_TAG": "CREATE TABLE SERVICE_TAG ( ID INT AUTO_INCREMENT PRIMARY KEY, TAG_ID INT, SERVICE_ID INT, CONSTRAINT FK_TAGSERVICE FOREIGN KEY (TAG_ID) REFERENCES TAG(ID), CONSTRAINT FK_SERVICETAG FOREIGN KEY (SERVICE_ID) REFERENCES SERVICE(ID));",
    "USER_TAG": "CREATE TABLE USER_TAG ( ID INT AUTO_INCREMENT PRIMARY KEY, TAG_ID INT, USER_ID VARCHAR(100), CONSTRAINT FK_TAGUSER FOREIGN KEY (TAG_ID) REFERENCES TAG(ID), CONSTRAINT FK_USERTAG FOREIGN KEY (USER_ID) REFERENCES USERS(ID));"
}

CommonScripts={
    "CHECK_TABLE_EXISTS":"SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{0}'"
}

Role={
    "Create":"INSERT INTO ROLE (NAME) VALUES ('{0}')",
    "List":"SELECT * FROM ROLE",
    "Get":"SELECT * FROM ROLE WHERE ID = '{0}'",
    "Update":"UPDATE ROLE SET NAME = '{0}' WHERE ID = '{1}'",
    "Delete":"DELETE FROM ROLE WHERE ID = '{0}'"
}


CRM={
    "Create":"INSERT INTO CRM (NAME, DESCRIPTION, WEBSITE) VALUES ('{0}','{1}','{2}')",
    "List":"SELECT * FROM CRM",
    "Get":"SELECT * FROM CRM WHERE ID = '{0}'",
    "Update":"UPDATE CRM SET NAME = '{0}', DESCRIPTION = '{1}', WEBSITE = '{2}' WHERE ID = '{3}'",
    "Delete":"DELETE FROM CRM WHERE ID = '{0}'"
}

User={
    "Create":"INSERT INTO USERS (ID, USERNAME, FIRSTNAME, LASTNAME, PHONENUMBER, MOBILEPHONENUMBER) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')",
    "List":"SELECT * FROM USERS",
    "Get":"SELECT ID id, USERNAME username, FIRSTNAME firstName, LASTNAME lastName, PHONENUMBER phoneNumber, MOBILEPHONENUMBER mobilePhoneNumber FROM USERS WHERE ID = '{0}'",
    "Update":"UPDATE USERS SET FIRSTNAME = '{0}', LASTNAME = '{1}', PHONENUMBER = '{2}', MOBILEPHONENUMBER = '{3}' WHERE ID = '{4}'",
    "Delete":"DELETE FROM USERS WHERE ID = '{0}'"
}

# "SERVICE":"CREATE TABLE SERVICE ( ID INT AUTO_INCREMENT PRIMARY KEY, USER_ID VARCHAR(100) NOT NULL, CRM_ID INT NOT NULL, TITLE VARCHAR(255), DESCRIPTION VARCHAR(1000), CONSTRAINT FK_CRMSERVICE FOREIGN KEY (CRM_ID) REFERENCES CRM(ID), CONSTRAINT FK_USERSERVICE FOREIGN KEY (USER_ID) REFERENCES USERS(ID) );",
SERVICE={

}
# "VENUES":"CREATE TABLE VENUES ( ID INT AUTO_INCREMENT PRIMARY KEY, CRM_ID INT NOT NULL, NAME VARCHAR(255), DESCRIPTION VARCHAR(1000), PHONE_NUMBER VARCHAR(20), LATITUDE DOUBLE, LONGITUDE DOUBLE, ADDRESS VARCHAR(500), SUBURB VARCHAR(500), CITY VARCHAR(500), STATE VARCHAR(500), COUNTRY VARCHAR(500), POST_CODE VARCHAR(500), CONSTRAINT FK_CRMVENUE FOREIGN KEY (CRM_ID) REFERENCES CRM(ID));",
VENUES={

}
# "VENUES_OPEN_HOUR":"CREATE TABLE VENUES_OPEN_HOUR ( ID INT AUTO_INCREMENT PRIMARY KEY, VENUE_ID INT NOT NULL, DAY VARCHAR(3), OPEN_TIME TIME, CLOSE_TIME TIME, CONSTRAINT FK_VENUE_OPENHOUR FOREIGN KEY (VENUE_ID) REFERENCES VENUES(ID));",
VENUES_OPEN_HOUR={

}
# "TAG": "CREATE TABLE TAG ( ID INT AUTO_INCREMENT PRIMARY KEY, CRM_ID INT NOT NULL, NAME VARCHAR(255), CONSTRAINT FK_CRMTAG FOREIGN KEY (CRM_ID) REFERENCES CRM(ID));",
TAG={

}
# "SERVICE_TAG": "CREATE TABLE SERVICE_TAG ( ID INT AUTO_INCREMENT PRIMARY KEY, TAG_ID INT, SERVICE_ID INT, CONSTRAINT FK_TAGSERVICE FOREIGN KEY (TAG_ID) REFERENCES TAG(ID), CONSTRAINT FK_SERVICETAG FOREIGN KEY (SERVICE_ID) REFERENCES SERVICE(ID));",
SERVICE_TAG={

}
# "USER_TAG": "CREATE TABLE USER_TAG ( ID INT AUTO_INCREMENT PRIMARY KEY, TAG_ID INT, USER_ID VARCHAR(100), CONSTRAINT FK_TAGUSER FOREIGN KEY (TAG_ID) REFERENCES TAG(ID), CONSTRAINT FK_USERTAG FOREIGN KEY (USER_ID) REFERENCES USERS(ID));"
USER_TAG={

}

SetUpScripts = [
    # create all of the tables
    CreateTableScript["ROLE"],
    CreateTableScript["CRM"],
    CreateTableScript["USER"],
    CreateTableScript["SERVICE"],
    CreateTableScript["VENUES"],
    CreateTableScript["TAG"],
    CreateTableScript["SERVICE_TAG"],
    CreateTableScript["USER_TAG"],
    # create default role
    Role["Create"].format("USER"),
    Role["Create"].format("CRM_ADMIN"),
    Role["Create"].format("ADMIN"),
    # create default CRM
    CRM["Create"].format("NotSuiteBox","This is not SuiteBox","trollClient.suitebox.com")
]