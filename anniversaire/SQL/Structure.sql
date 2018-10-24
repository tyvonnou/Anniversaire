



CREATE TABLE `Personne` (
  `id` int(255) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(255) NOT NULL,
  `naissance` date DEFAULT NULL
) ;


CREATE TABLE `v2` (
`ID` int(255)
,`Nom` varchar(255)
,`Prenom` varchar(255)
,`Date de naissance` date
,`Âge` int(11)
,`Jours restants` int(11)
);

CREATE TABLE `v2_notnull` (
`ID` int(255)
,`Nom` varchar(255)
,`Prenom` varchar(255)
,`Date de naissance` date
,`Âge` int(11)
,`Jours restants` int(11)
);


DROP TABLE IF EXISTS `v2`;

CREATE VIEW `v2`  AS  select `Personne`.`id` AS `ID`,`Personne`.`nom` AS `Nom`,`Personne`.`prenom` AS `Prenom`,`Personne`.`naissance` AS `Date de naissance`,`AGE`(`Personne`.`naissance`) AS `Âge`,`jrest`(`Personne`.`naissance`) AS `Jours restants` from `Personne` ;


DROP TABLE IF EXISTS `v2_notnull`;

CREATE VIEW `v2_notnull`  AS  select `Personne`.`id` AS `ID`,`Personne`.`nom` AS `Nom`,`Personne`.`prenom` AS `Prenom`,`Personne`.`naissance` AS `Date de naissance`,`AGE`(`Personne`.`naissance`) AS `Âge`,`jrest`(`Personne`.`naissance`) AS `Jours restants` from `Personne` where (`Personne`.`naissance` is not null) ;


ALTER TABLE `Personne`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `Personne`
  UPDATE `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

