/*
Navicat MySQL Data Transfer

Source Server         : 
Source Server Version : 
Source Host           : 
Source Database       : 

Target Server Type    : MYSQL
Target Server Version : 50641
File Encoding         : 65001

Date: 2018-08-23 05:59:56
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for good_model
-- ----------------------------
DROP TABLE IF EXISTS `good_model`;
CREATE TABLE `good_model` (
  `model_id` varchar(255) NOT NULL COMMENT '型号编号',
  `model_name` varchar(255) DEFAULT NULL COMMENT '货名',
  `model_number` varchar(255) DEFAULT NULL COMMENT '型号',
  `nuture` varchar(255) DEFAULT NULL COMMENT '属性',
  `other` varchar(255) DEFAULT NULL COMMENT '其他配件',
  `gs_code` int(10) DEFAULT NULL COMMENT '供货商编号',
  `sts` varchar(255) DEFAULT NULL COMMENT '型号状态 1.合作 2.备选 3.预选 4.结束',
  PRIMARY KEY (`model_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for good_supplier
-- ----------------------------
DROP TABLE IF EXISTS `good_supplier`;
CREATE TABLE `good_supplier` (
  `gs_code` int(10) NOT NULL AUTO_INCREMENT COMMENT '登记编号',
  `supplier` varchar(255) DEFAULT NULL COMMENT '供货商',
  `short_name` varchar(255) DEFAULT NULL COMMENT '简称',
  `linkman` varchar(255) DEFAULT NULL COMMENT '联系人',
  `telephone` varchar(255) DEFAULT NULL COMMENT '电话',
  `address` varchar(255) DEFAULT NULL COMMENT '地址',
  `other` varchar(255) DEFAULT NULL COMMENT '其他',
  `sts` varchar(255) DEFAULT NULL COMMENT '供应商状态1.合作 2.备选 3.预选 4.结束',
  PRIMARY KEY (`gs_code`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for goods
-- ----------------------------
DROP TABLE IF EXISTS `goods`;
CREATE TABLE `goods` (
  `id` int(11) NOT NULL COMMENT '登记编号',
  `goods_id` varchar(255) DEFAULT NULL COMMENT '资产编号',
  `SN` varchar(255) DEFAULT NULL COMMENT 'S/N编码',
  `model_id` varchar(255) DEFAULT NULL COMMENT '型号编号',
  `in_time` datetime DEFAULT NULL COMMENT '入库时间',
  `out_time` datetime DEFAULT NULL COMMENT '出库时间',
  `price_get` varchar(255) DEFAULT NULL COMMENT '采购价格',
  `price_sall` varchar(255) DEFAULT NULL COMMENT '销售价格',
  `status` varchar(255) DEFAULT NULL COMMENT '使用项目',
  `sts` varchar(255) DEFAULT NULL COMMENT '使用状态1.未出库 2.内部用 3.已销售 4.预占用',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for goods_log
-- ----------------------------
DROP TABLE IF EXISTS `goods_log`;
CREATE TABLE `goods_log` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `goods_id` varchar(255) DEFAULT NULL COMMENT '货物编号 货物关联编号',
  `create_time` datetime DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL COMMENT '最新状态',
  `sts` varchar(255) DEFAULT NULL COMMENT '状态类型 1.入库 2.出库 3.更新 4.退库',
  `tag` varchar(255) DEFAULT NULL COMMENT '最新标记 0.历史 1.最新',
  `man_register` varchar(255) DEFAULT NULL COMMENT '经手人 关联登录账户',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for msg_log
-- ----------------------------
DROP TABLE IF EXISTS `msg_log`;
CREATE TABLE `msg_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自动短信日志',
  `msgnum` varchar(255) DEFAULT NULL COMMENT '短信号码',
  `msgtxt` varchar(255) DEFAULT NULL COMMENT '短信内容',
  `sts` varchar(255) DEFAULT NULL COMMENT '发送状态：1.成功 2.失败',
  `user` varchar(255) DEFAULT NULL COMMENT '用户',
  `create_time` datetime DEFAULT NULL COMMENT '短信时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `user` varchar(255) DEFAULT NULL COMMENT '用户',
  `code` varchar(255) NOT NULL DEFAULT '' COMMENT '代号',
  `password` varchar(255) DEFAULT NULL COMMENT '密码',
  `telephone` varchar(255) DEFAULT NULL COMMENT '电话',
  `create_time` datetime(6) DEFAULT NULL COMMENT '更新时间',
  `sts` tinyint(10) DEFAULT NULL COMMENT '状态 0.在用 1.不在用',
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
