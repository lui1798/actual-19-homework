## 功能及实现方式：

```
1. 登陆功能：末登录跳转至登录页面，不能进行相关操作；
2. 资产添加功能：添加资产信息, 通过jQuery对主机名进行判断，为空提示出错 [POST]；
3. 资产查看功能：点击查看按钮，显示该资产详细信息，查不允许修改 [GET]；
4. 资产编辑功能：点击编辑按钮，显示该资产的信息，可进行资料修改 [PUT]；
5. 资产删除功能：点击删除按钮，删除该资产 [DELETE]；
6. 资产搜索功能：对计算机名进行资产搜索 [GET]；

```
## 数据库信息：
    库名：oprsys
    用户：proj
    密码：123456
## 模拟数据插入
    INSERT INTO `assets` VALUES (18, 'XMLT-ICCTEST-203', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '32G', '500G', '192.168.99.203', '127.0.0.1', '192.168.99.203', 'admin', 1, 'CentOS 7.2', 'ICC', 'XMLT-6-8', '', '2018-10-31 17:24:59', '2018-10-31 17:24:59');
    INSERT INTO `assets` VALUES (33, 'XMLT-ICCTEST-20', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '32G', '500G', '192.168.99.20', '127.0.0.1', '192.168.99.20', 'admin', 1, 'CentOS 7.2', 'ICC', 'XMLT-6-8', 'icc', '2018-10-31 17:24:59', '2018-10-31 17:24:59');
    INSERT INTO `assets` VALUES (34, 'XMLT-ICCTEST-21', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '32G', '500G', '192.168.99.21', '127.0.0.1', '192.168.99.21', 'admin', 1, 'CentOS 7.2', 'ICC', 'XMLT-6-9', 'icc', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (35, 'XMLT-ICCTEST-22', 64, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '32G', '500G', '192.168.99.22', '127.0.0.1', '192.168.99.22', 'admin', 0, 'CentOS 7.2', 'ICC', 'XMLT-6-10', 'icc', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (36, 'XMLT-ICCTEST-23', 64, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '32G', '100G', '192.168.99.23', '127.0.0.1', '192.168.99.23', 'admin', 1, 'CentOS 7.2', 'ICC', 'XMLT-6-11', 'sap', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (37, 'XMLT-ICCTEST-24', 64, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '32G', '500G', '192.168.99.24', '127.0.0.1', '192.168.99.24', 'admin', 0, 'CentOS 6.8', 'ICC', 'XMLT-6-12', 'icc', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (38, 'XMLT-ICCTEST-25', 64, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '32G', '200G', '192.168.99.25', '127.0.0.1', '192.168.99.25', 'admin', 1, 'CentOS 7.2', 'ICC', 'XMLT-6-13', 'sap', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (39, 'XMLT-ICCTEST-26', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '32G', '500G', '192.168.99.26', '127.0.0.1', '192.168.99.26', 'admin', 1, 'CentOS 7.2', 'ICC', 'XMLT-6-14', 'sap', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (40, 'XMLT-ICCTEST-27', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '32G', '500G', '192.168.99.27', '127.0.0.1', '192.168.99.27', 'admin', 0, 'CentOS 7.2', 'ICC', 'XMLT-6-15', 'sap', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (41, 'XMLT-ICCTEST-28', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '32G', '500G', '192.168.99.28', '127.0.0.1', '192.168.99.28', 'admin', 0, 'CentOS 7.2', 'ICC', 'XMLT-6-16', 'icc', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (42, 'XMLT-ICCTEST-29', 32, 'Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.10GHz', '64G', '300G', '192.168.99.29', '127.0.0.1', '192.168.99.29', 'admin', 1, 'CentOS 6.8', 'ICC', 'XMLT-6-17', 'icc', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (43, 'XMLT-ICCTEST-30', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '32G', '300G', '192.168.99.30', '127.0.0.1', '192.168.99.30', 'admin', 1, 'CentOS 7.2', 'ICC', 'XMLT-6-18', 'sap', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (44, 'XMLT-ICCTEST-31', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '128', '500G', '192.168.99.31', '127.0.0.1', '192.168.99.31', 'admin', 0, 'CentOS 7.2', 'ICC', 'XMLT-6-19', 'icc', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (45, 'XMLT-ICCTEST-32', 32, 'Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.10GHz', '32G', '200G', '192.168.99.32', '127.0.0.1', '192.168.99.32', 'admin', 1, 'CentOS 6.8', 'ICC', 'XMLT-6-20', 'icc', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (46, 'XMLT-ICCTEST-33', 64, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '32G', '500G', '192.168.99.33', '127.0.0.1', '192.168.99.33', 'admin', 0, 'CentOS 6.8', 'ICC', 'XMLT-6-21', 'sap', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (47, 'XMLT-ICCTEST-34', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '32G', '200G', '192.168.99.34', '127.0.0.1', '192.168.99.34', 'admin', 1, 'CentOS 7.2', 'ICC', 'XMLT-6-22', 'icc', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (48, 'XMLT-ICCTEST-35', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '256', '500G', '192.168.99.35', '127.0.0.1', '192.168.99.35', 'admin', 1, 'CentOS 7.2', 'ICC', 'XMLT-6-23', 'icc', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (50, 'XMLT-ICCTEST-37', 24, 'Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.10GHz', '256', '500G', '192.168.99.37', '127.0.0.1', '192.168.99.37', 'admin', 0, 'CentOS 6.8', 'ICC', 'XMLT-6-25', 'icc', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (51, 'XMLT-ICCTEST-38', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '32G', '500G', '192.168.99.38', '127.0.0.1', '192.168.99.38', 'admin', 1, 'CentOS 7.2', 'ICC', 'XMLT-6-26', 'icc', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (52, 'XMLT-ICCTEST-39', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '32G', '200G', '192.168.99.39', '127.0.0.1', '192.168.99.39', 'admin', 1, 'CentOS 7.2', 'ICC', 'XMLT-6-27', 'icc', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (53, 'XMLT-ICCTEST-40', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '64G', '600G', '192.168.99.40', '127.0.0.1', '192.168.99.40', 'admin', 0, 'CentOS 7.2', 'ICC', 'XMLT-6-28', 'icc', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (54, 'XMLT-ICCTEST-41', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '64G', '500G', '192.168.99.41', '127.0.0.1', '192.168.99.41', 'admin', 1, 'CentOS 6.8', 'ICC', 'XMLT-6-29', 'icc', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (55, 'XMLT-ICCTEST-42', 64, 'Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.10GHz', '32G', '500G', '192.168.99.42', '127.0.0.1', '192.168.99.42', 'admin', 1, 'CentOS 7.2', 'ICC', 'XMLT-6-30', 'sap', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (56, 'XMLT-ICCTEST-43', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '64G', '600G', '192.168.99.43', '127.0.0.1', '192.168.99.43', 'admin', 0, 'CentOS 7.2', 'ICC', 'XMLT-6-31', 'sap', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (57, 'XMLT-ICCTEST-44', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '32G', '500G', '192.168.99.44', '127.0.0.1', '192.168.99.44', 'admin', 1, 'CentOS 6.8', 'ICC', 'XMLT-6-32', 'icc', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (58, 'XMLT-ICCTEST-45', 64, 'Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.10GHz', '32G', '500G', '192.168.99.45', '127.0.0.1', '192.168.99.45', 'admin', 1, 'CentOS 7.2', 'ICC', 'XMLT-6-33', 'icc', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (59, 'XMLT-ICCTEST-46', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '128', '500G', '192.168.99.46', '127.0.0.1', '192.168.99.46', 'admin', 1, 'CentOS 6.8', 'ICC', 'XMLT-6-34', 'icc', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (60, 'XMLT-ICCTEST-47', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '32G', '500G', '192.168.99.47', '127.0.0.1', '192.168.99.47', 'admin', 1, 'CentOS 7.2', 'ICC', 'XMLT-6-35', 'sap', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (61, 'XMLT-ICCTEST-48', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '32G', '500G', '192.168.99.48', '127.0.0.1', '192.168.99.48', 'admin', 0, 'CentOS 7.2', 'ICC', 'XMLT-6-36', 'icc', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (62, 'XMLT-ICCTEST-49', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '32G', '500G', '192.168.99.49', '127.0.0.1', '192.168.99.49', 'admin', 1, 'CentOS 7.2', 'ICC', 'XMLT-6-37', 'sap1111', '2018-11-01 04:45:23', '2018-11-01 04:45:23');
    INSERT INTO `assets` VALUES (65, 'XMLT-ICCTEST-202', 32, 'Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz', '32G', '500G', '192.168.99.202', '127.0.0.1', '192.168.99.202', 'admin', 1, 'CentOS 7.2', 'ICC', 'XMLT-6-333', '', '2018-11-02 02:47:20', '2018-11-02 02:47:20');