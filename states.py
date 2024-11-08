transitions = {
('q0', '2'): ('2', 'R', 'q1'),
('q0', '4'): ('4', 'R', 'q1'),
('q0', '0'): ('0', 'R', 'q1'),
('q0', '9'): ('9', 'R', 'q1'),
('q0', '1'): ('1', 'R', 'q1'),
('q0', '6'): ('6', 'R', 'q1'),
('q0', '5'): ('5', 'R', 'q1'),
('q0', '8'): ('8', 'R', 'q1'),
('q0', '3'): ('3', 'R', 'q1'),
('q0', '7'): ('7', 'R', 'q1'),
('q1', '1'): ('1', 'R', 'q2'),
('q1', '6'): ('6', 'R', 'q2'),
('q1', '2'): ('2', 'R', 'q2'),
('q1', '3'): ('3', 'R', 'q2'),
('q1', '0'): ('0', 'R', 'q2'),
('q1', '4'): ('4', 'R', 'q2'),
('q1', '9'): ('9', 'R', 'q2'),
('q1', '8'): ('8', 'R', 'q2'),
('q1', '7'): ('7', 'R', 'q2'),
('q1', '5'): ('5', 'R', 'q2'),
('q2', '0'): ('0', 'R', 'q3'),
('q2', '7'): ('7', 'R', 'q3'),
('q2', '3'): ('3', 'R', 'q3'),
('q2', '9'): ('9', 'R', 'q3'),
('q2', '6'): ('6', 'R', 'q3'),
('q2', '1'): ('1', 'R', 'q3'),
('q2', '5'): ('5', 'R', 'q3'),
('q2', '2'): ('2', 'R', 'q3'),
('q2', '4'): ('4', 'R', 'q3'),
('q2', '8'): ('8', 'R', 'q3'),
('q2', '/'): ('/', 'R', 'q5'),
('q3', '/'): ('/', 'R', 'q5'),
('q3', '8'): ('8', 'R', 'q4'),
('q3', '7'): ('7', 'R', 'q4'),
('q3', '0'): ('0', 'R', 'q4'),
('q3', '9'): ('9', 'R', 'q4'),
('q3', '6'): ('6', 'R', 'q4'),
('q3', '2'): ('2', 'R', 'q4'),
('q3', '4'): ('4', 'R', 'q4'),
('q3', '3'): ('3', 'R', 'q4'),
('q3', '1'): ('1', 'R', 'q4'),
('q3', '5'): ('5', 'R', 'q4'),
('q4', '/'): ('/', 'R', 'q5'),
('q5', 't'): ('t', 'R', 'q6'),
('q5', 'u'): ('u', 'R', 'q9'),
('q6', 'c'): ('c', 'R', 'q7'),
('q7', 'p'): ('p', 'R', 'q8'),
('q8', '-'): ('-', 'R', 'q16'),
('q9', 'd'): ('d', 'R', 'q10'),
('q10', 'p'): ('p', 'R', 'q8'),
('q11', 'p'): ('p', 'R', 'q12'),
('q12', 'e'): ('e', 'R', 'q13'),
('q13', 'n'): ('n', 'R', 'q14'),
('q14', '-'): ('-', 'R', 'q15'),
('q15', 'm'): ('m', 'R', 'q68'),
('q15', 'd'): ('d', 'R', 'q316'),
('q15', 'i'): ('i', 'R', 'q60'),
('q15', 't'): ('t', 'R', 'q23'),
('q15', 'n'): ('n', 'R', 'q34'),
('q15', 'h'): ('h', 'R', 'q41'),
('q15', 'f'): ('f', 'R', 'q17'),
('q15', 's'): ('s', 'R', 'q20'),
('q15', 'p'): ('p', 'R', 'q115'),
('q15', 'l'): ('l', 'R', 'q64'),
('q15', 'v'): ('v', 'R', 'q125'),
('q16', 'o'): ('o', 'R', 'q11'),
('q17', 't'): ('t', 'R', 'q18'),
('q18', 'p'): ('p', 'R', 'q19'),
('q19', ' '): (':', 'R', 'q155'),
('q20', 'n'): ('n', 'R', 'q70'),
('q20', 's'): ('s', 'R', 'q21'),
('q20', 'm'): ('m', 'R', 'q35'),
('q21', 'h'): ('h', 'R', 'q22'),
('q22', ' '): (':', 'R', 'q182'),
('q23', 'e'): ('e', 'R', 'q24'),
('q24', 'l'): ('l', 'R', 'q25'),
('q25', 'n'): ('n', 'R', 'q26'),
('q26', 'e'): ('e', 'R', 'q27'),
('q27', 't'): ('t', 'R', 'q33'),
('q28', ' '): ('a', 'R', 'q29'),
('q29', ' '): ('t', 'R', 'q30'),
('q30', ' '): ('t', 'R', 'q32'),
('q31', ' '): ('u', 'R', 'q192'),
('q32', ' '): ('a', 'R', 'q191'),
('q33', ' '): (':', 'R', 'q73'),
('q34', 'e'): ('e', 'R', 'q50'),
('q35', 't'): ('t', 'R', 'q36'),
('q36', 'p'): ('p', 'R', 'q37'),
('q37', ' '): (':', 'R', 'q217'),
('q38', ' '): ('n', 'R', 'q137'),
('q39', ' '): ('u', 'R', 'q40'),
('q40', ' '): ('r', 'R', 'q181'),
('q41', 't'): ('t', 'R', 'q42'),
('q42', 't'): ('t', 'R', 'q43'),
('q43', 'p'): ('p', 'R', 'q44'),
('q44', 's'): ('s', 'R', 'q45'),
('q44', '-'): ('-', 'R', 'q128'),
('q44', ' '): (':', 'R', 'q83'),
('q45', ' '): (':', 'R', 'q83'),
('q46', 'c'): ('c', 'R', 'q293'),
('q47', 'p'): ('p', 'R', 'q46'),
('q48', '3'): ('3', 'R', 'q49'),
('q49', 's'): ('s', 'R', 'q91'),
('q49', ' '): (':', 'R', 'q28'),
('q50', 't'): ('t', 'R', 'q51'),
('q51', 'b'): ('b', 'R', 'q52'),
('q52', 'i'): ('i', 'R', 'q53'),
('q53', 'o'): ('o', 'R', 'q54'),
('q54', 's'): ('s', 'R', 'q55'),
('q55', '-'): ('-', 'R', 'q56'),
('q56', 's'): ('s', 'R', 'q57'),
('q57', 's'): ('s', 'R', 'q58'),
('q58', 'n'): ('n', 'R', 'q59'),
('q59', ' '): (':', 'R', 'q254'),
('q60', 'm'): ('m', 'R', 'q61'),
('q61', 'a'): ('a', 'R', 'q62'),
('q62', 'p'): ('p', 'R', 'q63'),
('q63', 's'): ('s', 'R', 'q104'),
('q63', ' '): (':', 'R', 'q28'),
('q64', 'd'): ('d', 'R', 'q65'),
('q65', 'a'): ('a', 'R', 'q66'),
('q66', 'p'): ('p', 'R', 'q67'),
('q67', ' '): (':', 'R', 'q276'),
('q68', 'i'): ('i', 'R', 'q69'),
('q68', 's'): ('s', 'R', 'q93'),
('q68', 'y'): ('y', 'R', 'q100'),
('q69', 'c'): ('c', 'R', 'q74'),
('q70', 'm'): ('m', 'R', 'q71'),
('q71', 'p'): ('p', 'R', 'q72'),
('q72', ' '): (':', 'R', 'q230'),
('q73', ' '): ('a', 'R', 'q143'),
('q74', 'r'): ('r', 'R', 'q75'),
('q75', 'o'): ('o', 'R', 'q76'),
('q76', 's'): ('s', 'R', 'q77'),
('q77', 'o'): ('o', 'R', 'q78'),
('q78', 'f'): ('f', 'R', 'q79'),
('q79', 't'): ('t', 'R', 'q92'),
('q80', 'd'): ('d', 'R', 'q81'),
('q81', 's'): ('s', 'R', 'q82'),
('q82', ' '): (':', 'R', 'q239'),
('q83', ' '): ('i', 'R', 'q84'),
('q84', ' '): ('n', 'R', 'q85'),
('q85', ' '): ('y', 'R', 'q86'),
('q86', ' '): ('e', 'R', 'q134'),
('q87', ' '): ('e', 'R', 'q88'),
('q88', ' '): ('x', 'R', 'q89'),
('q89', ' '): ('p', 'R', 'q90'),
('q90', ' '): ('l', 'R', 'q226'),
('q91', ' '): (':', 'R', 'q204'),
('q92', '-'): ('-', 'R', 'q80'),
('q93', 'r'): ('r', 'R', 'q47'),
('q93', '-'): ('-', 'R', 'q94'),
('q94', 'w'): ('w', 'R', 'q105'),
('q94', 's'): ('s', 'R', 'q95'),
('q95', 'q'): ('q', 'R', 'q96'),
('q96', 'l'): ('l', 'R', 'q97'),
('q97', '-'): ('-', 'R', 'q98'),
('q98', 's'): ('s', 'R', 'q99'),
('q99', ' '): (':', 'R', 'q83'),
('q100', 's'): ('s', 'R', 'q101'),
('q101', 'q'): ('q', 'R', 'q102'),
('q102', 'l'): ('l', 'R', 'q103'),
('q103', ' '): (':', 'R', 'q83'),
('q104', ' '): (':', 'R', 'q204'),
('q105', 'b'): ('b', 'R', 'q106'),
('q106', 't'): ('t', 'R', 'q107'),
('q107', '-'): ('-', 'R', 'q108'),
('q108', 's'): ('s', 'R', 'q109'),
('q109', 'e'): ('e', 'R', 'q110'),
('q110', 'r'): ('r', 'R', 'q111'),
('q111', 'v'): ('v', 'R', 'q112'),
('q112', 'e'): ('e', 'R', 'q113'),
('q113', 'r'): ('r', 'R', 'q114'),
('q114', ' '): (':', 'R', 'q87'),
('q115', 'o'): ('o', 'R', 'q116'),
('q116', 's'): ('s', 'R', 'q117'),
('q116', 'p'): ('p', 'R', 'q48'),
('q117', 't'): ('t', 'R', 'q118'),
('q118', 'g'): ('g', 'R', 'q119'),
('q119', 'r'): ('r', 'R', 'q120'),
('q120', 'e'): ('e', 'R', 'q121'),
('q121', 's'): ('s', 'R', 'q122'),
('q122', 'q'): ('q', 'R', 'q123'),
('q123', 'l'): ('l', 'R', 'q124'),
('q124', ' '): (':', 'R', 'q83'),
('q125', 'n'): ('n', 'R', 'q126'),
('q126', 'c'): ('c', 'R', 'q127'),
('q127', ' '): (':', 'R', 'q73'),
('q128', 'p'): ('p', 'R', 'q129'),
('q129', 'r'): ('r', 'R', 'q130'),
('q130', 'o'): ('o', 'R', 'q131'),
('q131', 'x'): ('x', 'R', 'q132'),
('q132', 'y'): ('y', 'R', 'q133'),
('q133', ' '): (':', 'R', 'q83'),
('q134', ' '): ('c', 'R', 'q135'),
('q135', ' '): ('c', 'R', 'q136'),
('q136', ' '): ('i', 'R', 'q138'),
('q137', ' '): ('-', 'R', 'q139'),
('q138', ' '): ('o', 'R', 'q38'),
('q139', ' '): ('S', 'R', 'q140'),
('q140', ' '): ('Q', 'R', 'q141'),
('q141', ' '): ('L', 'R', 'q142'),
('q143', ' '): ('t', 'R', 'q144'),
('q144', ' '): ('a', 'R', 'q145'),
('q145', ' '): ('q', 'R', 'q146'),
('q146', ' '): ('u', 'R', 'q147'),
('q147', ' '): ('e', 'R', 'q148'),
('q148', ' '): ('s', 'R', 'q149'),
('q149', ' '): ('-', 'R', 'q150'),
('q150', ' '): ('M', 'R', 'q151'),
('q151', ' '): ('I', 'R', 'q152'),
('q152', ' '): ('T', 'R', 'q153'),
('q153', ' '): ('M', 'R', 'q154'),
('q155', ' '): ('t', 'R', 'q156'),
('q156', ' '): ('r', 'R', 'q157'),
('q157', ' '): ('a', 'R', 'q158'),
('q158', ' '): ('s', 'R', 'q159'),
('q159', ' '): ('f', 'R', 'q160'),
('q160', ' '): ('e', 'R', 'q161'),
('q161', ' '): ('r', 'R', 'q162'),
('q162', ' '): ('e', 'R', 'q163'),
('q163', ' '): ('n', 'R', 'q164'),
('q164', ' '): ('c', 'R', 'q165'),
('q165', ' '): ('i', 'R', 'q166'),
('q166', ' '): ('a', 'R', 'q167'),
('q167', ' '): ('-', 'R', 'q168'),
('q168', ' '): ('s', 'R', 'q169'),
('q169', ' '): ('i', 'R', 'q170'),
('q170', ' '): ('n', 'R', 'q171'),
('q171', ' '): ('-', 'R', 'q172'),
('q172', ' '): ('c', 'R', 'q173'),
('q173', ' '): ('i', 'R', 'q174'),
('q174', ' '): ('f', 'R', 'q175'),
('q175', ' '): ('r', 'R', 'q176'),
('q176', ' '): ('a', 'R', 'q178'),
('q177', ' '): ('s', 'R', 'q229'),
('q178', ' '): ('d', 'R', 'q179'),
('q179', ' '): ('o', 'R', 'q180'),
('q181', ' '): ('a', 'R', 'q245'),
('q182', ' '): ('e', 'R', 'q183'),
('q183', ' '): ('x', 'R', 'q184'),
('q184', ' '): ('p', 'R', 'q185'),
('q185', ' '): ('l', 'R', 'q186'),
('q186', ' '): ('o', 'R', 'q187'),
('q187', ' '): ('i', 'R', 'q188'),
('q188', ' '): ('t', 'R', 'q189'),
('q189', ' '): ('s', 'R', 'q190'),
('q191', ' '): ('q', 'R', 'q31'),
('q192', ' '): ('e', 'R', 'q194'),
('q193', ' '): ('-', 'R', 'q196'),
('q194', ' '): ('s', 'R', 'q193'),
('q195', ' '): ('f', 'R', 'q197'),
('q196', ' '): ('s', 'R', 'q200'),
('q197', ' '): ('f', 'R', 'q198'),
('q198', ' '): ('i', 'R', 'q201'),
('q199', ' '): ('i', 'R', 'q195'),
('q200', ' '): ('n', 'R', 'q199'),
('q201', ' '): ('n', 'R', 'q202'),
('q202', ' '): ('g', 'R', 'q203'),
('q204', ' '): ('c', 'R', 'q205'),
('q205', ' '): ('o', 'R', 'q206'),
('q206', ' '): ('n', 'R', 'q207'),
('q207', ' '): ('f', 'R', 'q208'),
('q208', ' '): ('.', 'R', 'q209'),
('q209', ' '): ('S', 'R', 'q210'),
('q210', ' '): ('S', 'R', 'q211'),
('q211', ' '): ('L', 'R', 'q212'),
('q212', ' '): ('/', 'R', 'q213'),
('q213', ' '): ('T', 'R', 'q214'),
('q214', ' '): ('L', 'R', 'q215'),
('q215', ' '): ('S', 'R', 'q216'),
('q217', ' '): ('s', 'R', 'q218'),
('q218', ' '): ('p', 'R', 'q219'),
('q219', ' '): ('o', 'R', 'q220'),
('q220', ' '): ('o', 'R', 'q221'),
('q221', ' '): ('f', 'R', 'q222'),
('q222', ' '): ('i', 'R', 'q223'),
('q223', ' '): ('n', 'R', 'q224'),
('q224', ' '): ('g', 'R', 'q225'),
('q226', ' '): ('o', 'R', 'q227'),
('q227', ' '): ('i', 'R', 'q228'),
('q228', ' '): ('t', 'R', 'q177'),
('q230', ' '): ('i', 'R', 'q231'),
('q231', ' '): ('n', 'R', 'q232'),
('q232', ' '): ('f', 'R', 'q233'),
('q233', ' '): ('o', 'R', 'q234'),
('q234', ' '): ('-', 'R', 'q235'),
('q235', ' '): ('r', 'R', 'q236'),
('q236', ' '): ('e', 'R', 'q237'),
('q237', ' '): ('d', 'R', 'q238'),
('q239', ' '): ('r', 'R', 'q240'),
('q240', ' '): ('e', 'R', 'q241'),
('q241', ' '): ('d', 'R', 'q242'),
('q242', ' '): ('-', 'R', 'q244'),
('q243', ' '): ('l', 'R', 'q247'),
('q244', ' '): ('m', 'R', 'q246'),
('q245', ' '): ('d', 'R', 'q291'),
('q246', ' '): ('a', 'R', 'q243'),
('q247', ' '): ('-', 'R', 'q248'),
('q248', ' '): ('c', 'R', 'q249'),
('q249', ' '): ('o', 'R', 'q250'),
('q250', ' '): ('n', 'R', 'q251'),
('q251', ' '): ('f', 'R', 'q252'),
('q252', ' '): ('i', 'R', 'q253'),
('q253', ' '): ('g', 'R', 'q39'),
('q254', ' '): ('c', 'R', 'q255'),
('q255', ' '): ('o', 'R', 'q256'),
('q256', ' '): ('m', 'R', 'q257'),
('q257', ' '): ('p', 'R', 'q258'),
('q258', ' '): ('a', 'R', 'q259'),
('q259', ' '): ('r', 'R', 'q260'),
('q260', ' '): ('t', 'R', 'q261'),
('q261', ' '): ('i', 'R', 'q262'),
('q262', ' '): ('r', 'R', 'q263'),
('q263', ' '): ('-', 'R', 'q264'),
('q264', ' '): ('a', 'R', 'q265'),
('q265', ' '): ('r', 'R', 'q266'),
('q266', ' '): ('c', 'R', 'q267'),
('q267', ' '): ('h', 'R', 'q268'),
('q268', ' '): ('i', 'R', 'q269'),
('q269', ' '): ('v', 'R', 'q270'),
('q270', ' '): ('o', 'R', 'q271'),
('q271', ' '): ('-', 'R', 'q272'),
('q272', ' '): ('r', 'R', 'q273'),
('q273', ' '): ('e', 'R', 'q274'),
('q274', ' '): ('d', 'R', 'q275'),
('q276', ' '): ('i', 'R', 'q277'),
('q277', ' '): ('n', 'R', 'q278'),
('q278', ' '): ('y', 'R', 'q279'),
('q279', ' '): ('e', 'R', 'q280'),
('q280', ' '): ('c', 'R', 'q281'),
('q281', ' '): ('c', 'R', 'q282'),
('q282', ' '): ('i', 'R', 'q283'),
('q283', ' '): ('o', 'R', 'q284'),
('q284', ' '): ('n', 'R', 'q285'),
('q285', ' '): ('-', 'R', 'q286'),
('q286', ' '): ('L', 'R', 'q287'),
('q287', ' '): ('D', 'R', 'q288'),
('q288', ' '): ('A', 'R', 'q289'),
('q289', ' '): ('P', 'R', 'q290'),
('q291', ' '): ('a', 'R', 'q292'),
('q293', ' '): (':', 'R', 'q294'),
('q294', ' '): ('d', 'R', 'q295'),
('q295', ' '): ('e', 'R', 'q296'),
('q296', ' '): ('n', 'R', 'q297'),
('q297', ' '): ('e', 'R', 'q298'),
('q298', ' '): ('g', 'R', 'q299'),
('q299', ' '): ('a', 'R', 'q300'),
('q300', ' '): ('c', 'R', 'q301'),
('q301', ' '): ('i', 'R', 'q302'),
('q302', ' '): ('o', 'R', 'q303'),
('q303', ' '): ('n', 'R', 'q304'),
('q304', ' '): ('-', 'R', 'q305'),
('q305', ' '): ('d', 'R', 'q306'),
('q306', ' '): ('e', 'R', 'q307'),
('q307', ' '): ('-', 'R', 'q308'),
('q308', ' '): ('s', 'R', 'q309'),
('q309', ' '): ('e', 'R', 'q310'),
('q310', ' '): ('r', 'R', 'q311'),
('q311', ' '): ('v', 'R', 'q312'),
('q312', ' '): ('i', 'R', 'q313'),
('q313', ' '): ('c', 'R', 'q314'),
('q314', ' '): ('i', 'R', 'q315'),
('q315', ' '): ('o', 'R', 'q203'),
('q316', 'n'): ('n', 'R', 'q317'),
('q317', 's'): ('s', 'R', 'q318'),
('q318', ' '): (':', 'R', 'q319'),
('q319', ' '): ('a', 'R', 'q320'),
('q320', ' '): ('m', 'R', 'q321'),
('q321', ' '): ('p', 'R', 'q322'),
('q322', ' '): ('l', 'R', 'q323'),
('q323', ' '): ('i', 'R', 'q324'),
('q324', ' '): ('f', 'R', 'q325'),
('q325', ' '): ('i', 'R', 'q326'),
('q326', ' '): ('c', 'R', 'q327'),
('q327', ' '): ('a', 'R', 'q328'),
('q328', ' '): ('c', 'R', 'q329'),
('q329', ' '): ('i', 'R', 'q330'),
('q330', ' '): ('o', 'R', 'q331'),
('q331', ' '): ('n', 'R', 'q332'),
('q332', ' '): ('-', 'R', 'q333'),
('q333', ' '): ('D', 'R', 'q334'),
('q334', ' '): ('D', 'R', 'q335'),
('q335', ' '): ('o', 'R', 'q336'),
('q336', ' '): ('S', 'R', 'q216'),
}

final_states = {'q142', 'q225', 'q238', 'q190', 'q180', 'q154', 'q142', 'q229', 'q253', 'q275', 'q290', 'q203', 'q216', 'q292'} 
initial_state = 'q0'