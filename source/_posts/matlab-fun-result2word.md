---
title: 转载 | Matlab 生成 Word 报告
date: 2016-11-10 20:47:34
categories:
  - Matlab
tags:
  - Matlab
---

最近在进行一批来料的检验测试，一个个手动填写报告存图片太慢了，就有了种想要使用 Matlab 在分析完后数据可以自动生成 PDF 报告的想法，于是就去网上搜索了相关的资料，发现[Matlab 中文论坛](http://www.ilovematlab.cn/)上有 xiezhh 曾经发过的使用 Matlab 生成 Word 的一些功能代码。又看了些 xiezhh 别的帖子和一些别的小伙伴的补充，找到了相关代码，经过运行可以完美的实现功能，在此表示感谢。

其中蕴含了基本的表格操作（如合并单元格）和图片复制粘贴操作，对于我这次的需求已经是足够了，代码部分下面部分列出，其中添加了个人阅读时的一些注释，有助于理解。现阶段我也只是可以根据该代码进行部分更改完成自己的需求，深层次的理解暂时还没有达到。

<!--more-->


```matlab

function fun_word
%利用MATLAB生成Word文档
%	原摘自xiezhh，根据论坛上的相关建议，做了稍微的改动和完善

filespec_user = [pwd '\测试.doc'];

%===启用word调用功能========================================================
try    
    Word = actxGetRunningServer('Word.Application');
catch    
    Word = actxserver('Word.Application'); 
end
Word.Visible = 1; % 使word为可见；或set(Word, 'Visible', 1); 
%===打开word文件，如果路径下没有则创建一个空白文档打开========================
if exist(filespec_user,'file'); 
    Document = Word.Documents.Open(filespec_user);    
else
    Document = Word.Documents.Add;     
    Document.SaveAs2(filespec_user);
end
%===格式定义===============================================================
Content = Document.Content;
Selection = Word.Selection;
Paragraphformat = Selection.ParagraphFormat;
%===文档的页边距===========================================================
Document.PageSetup.TopMargin    = 60;
Document.PageSetup.BottomMargin = 45;
Document.PageSetup.LeftMargin   = 45;
Document.PageSetup.RightMargin  = 45;
%==========================================================================

%===文档组成部分============================================================
% 文档的标题及格式
headline            = '报告';
Content.Start       = 0;    % 起始点为0，即表示每次写入覆盖之前资料
Content.Text        = headline;
Content.Font.Size   = 16;   % 字体大小
Content.Font.Bold   = 1;    % 字体加粗
Content.Paragraphs.Alignment = 'wdAlignParagraphCenter'; % 居中,wdAlignParagraphLeft/Center/Right

% 文档的创建时间
Selection.Start     = Content.end;  % 开始的地方在上一个的结尾
Selection.TypeParagraph;            % 插入一个新的空段落
% 插入时间
currentdate         = datestr(now, 0);  % 获取当前时间
Selection.Text      = currentdate;      % 当前时间作为输出
Selection.Font.Size = 12;               % 字号
Selection.Font.Bold = 0;                % 不加粗
Selection.MoveDown;                     %将所选内容向下移动，并返回移动距离的单位数
Paragraphformat.Alignment = 'wdAlignParagraphCenter'; % 居中

% 插入回车
Selection.TypeParagraph;% 插入一个新的空段落
Selection.Font.Size = 10.5;% 新的空段落字号

% 插入表格
Selection.Start     = Content.end;
Selection.TypeParagraph;
Paragraphformat.Alignment = 'wdAlignParagraphLeft';
Selection.MoveDown;

Tables = Document.Tables.Add(Selection.Range,12,9);    % 插入一个12行9列的表格

DTI = Document.Tables.Item(1); % 表格句柄

DTI.Borders.OutsideLineStyle    = 'wdLineStyleSingle';  % 最外框，实线
DTI.Borders.OutsideLineWidth    = 'wdLineWidth150pt';   % 线宽
DTI.Borders.InsideLineStyle     = 'wdLineStyleSingle';  % 所有的内框线条
DTI.Borders.InsideLineWidth     = 'wdLineWidth150pt';   % 线宽

DTI.Rows.Alignment                          = 'wdAlignRowCenter'; %大表格居中
DTI.Rows.Item(8).Borders.Item(1).LineStyle  = 'wdLineStyleNone'; % 第八行的上边线消失
DTI.Rows.Item(8).Borders.Item(3).LineStyle  = 'wdLineStyleNone';% 第八行的下边线消失
DTI.Rows.Item(11).Borders.Item(1).LineStyle = 'wdLineStyleNone';
DTI.Rows.Item(11).Borders.Item(3).LineStyle = 'wdLineStyleNone';

% 设置行高，列宽
column_width = [53.7736,85.1434,53.7736,35.0094,...
    35.0094,76.6981,55.1887,52.9245,54.9057];
row_height = [28.5849,28.5849,28.5849,28.5849,25.4717,25.4717,...
    32.8302,312.1698,17.8302,49.2453,14.1509,18.6792];

for i = 1:9
    DTI.Columns.Item(i).Width = column_width(i);
end

for i = 1:12
    DTI.Rows.Item(i).Height = row_height(i);
end

% 设置垂直居中
for i = 1:12        % 行
    for j = 1:9     % 列
        DTI.Cell(i,j).VerticalAlignment = 'wdCellAlignVerticalCenter';
    end
end

% 合并单元格
DTI.Cell(1, 4).Merge(DTI.Cell(1, 5)); % 第一行第四个到第五个合并
DTI.Cell(2, 4).Merge(DTI.Cell(2, 5));
DTI.Cell(3, 4).Merge(DTI.Cell(3, 5));
DTI.Cell(4, 4).Merge(DTI.Cell(4, 5));
DTI.Cell(5, 2).Merge(DTI.Cell(5, 5));
DTI.Cell(5, 3).Merge(DTI.Cell(5, 6));
DTI.Cell(6, 2).Merge(DTI.Cell(6, 5));
DTI.Cell(6, 3).Merge(DTI.Cell(6, 6));
DTI.Cell(5, 1).Merge(DTI.Cell(6, 1));
DTI.Cell(7, 1).Merge(DTI.Cell(7, 9));
DTI.Cell(8, 1).Merge(DTI.Cell(8, 9));
DTI.Cell(9, 1).Merge(DTI.Cell(9, 3));
DTI.Cell(9, 2).Merge(DTI.Cell(9, 3));
DTI.Cell(9, 3).Merge(DTI.Cell(9, 4));
DTI.Cell(9, 4).Merge(DTI.Cell(9, 5));
DTI.Cell(10, 1).Merge(DTI.Cell(10, 9));% 第10行第1个到第9个合并
DTI.Cell(11, 5).Merge(DTI.Cell(11, 9));
DTI.Cell(12, 5).Merge(DTI.Cell(12, 9));
DTI.Cell(11, 1).Merge(DTI.Cell(12, 4));


% 表格之后的段落
Selection.Start = Content.end;
Selection.TypeParagraph;
Selection.Text = '主管院长签字：            年    月    日';
Paragraphformat.Alignment = 'wdAlignParagraphRight';
Selection.MoveDown;

% 定义表格中的内容
DTI.Cell(1,1).Range.Text = '课程名称';
DTI.Cell(1,3).Range.Text = '课程号';
DTI.Cell(1,5).Range.Text = '任课教师学院';
DTI.Cell(1,7).Range.Text = '任课教师';
DTI.Cell(2,1).Range.Text = '授课班级';
DTI.Cell(2,3).Range.Text = '考试日期';
DTI.Cell(2,5).Range.Text = '应考人数';
DTI.Cell(2,7).Range.Text = '实考人数';
DTI.Cell(3,1).Range.Text = '出卷方式';
DTI.Cell(3,3).Range.Text = '阅卷方式';
DTI.Cell(3,5).Range.Text = '选用试卷A/B';
DTI.Cell(3,7).Range.Text = '考试时间';
DTI.Cell(4,1).Range.Text = '考试方式';
DTI.Cell(4,3).Range.Text = '平均分';
DTI.Cell(4,5).Range.Text = '不及格人数';
DTI.Cell(4,7).Range.Text = '及格率';
DTI.Cell(5,1).Range.Text = '成绩分布';
DTI.Cell(5,2).Range.Text = '90分以上      人占        %';
DTI.Cell(5,3).Range.Text = '80---89分        人占        %';
DTI.Cell(6,2).Range.Text = '70--79分      人占        %';
DTI.Cell(6,3).Range.Text = '60---69分        人占        %';
DTI.Cell(7,1).Range.Text = ['试卷分析（含是否符合教学大纲、难度、知识覆'...
    '盖面、班级分数分布分析、学生答题存在的共性问题与知识掌握情况、教学中'...
    '存在的问题及改进措施等内容）'];
DTI.Cell(7,1).Range.ParagraphFormat.Alignment = 'wdAlignParagraphLeft';
DTI.Cell(9,2).Range.Text = '签字 :';
DTI.Cell(9,4).Range.Text = '年    月    日';
DTI.Cell(10,1).Range.Text = '教研室审阅意见：';
DTI.Cell(10,1).Range.ParagraphFormat.Alignment = 'wdAlignParagraphLeft';
DTI.Cell(10,1).VerticalAlignment = 'wdCellAlignVerticalTop';
DTI.Cell(11,2).Range.Text = '教研室主任（签字）:          年    月    日';
DTI.Cell(11,2).Range.ParagraphFormat.Alignment = 'wdAlignParagraphLeft';
DTI.Cell(8,1).Range.ParagraphFormat.Alignment = 'wdAlignParagraphLeft';
DTI.Cell(8,1).VerticalAlignment = 'wdCellAlignVerticalTop';
DTI.Cell(9,2).Borders.Item(2).LineStyle = 'wdLineStyleNone';
DTI.Cell(9,2).Borders.Item(4).LineStyle = 'wdLineStyleNone';
DTI.Cell(9,3).Borders.Item(4).LineStyle = 'wdLineStyleNone';
DTI.Cell(11,1).Borders.Item(4).LineStyle = 'wdLineStyleNone';

% 暂时没搞懂意思，貌似不用也不影响
Shape = Document.Shapes;
ShapeCount = Shape.Count;
if ShapeCount ~= 0;
    for i = 1:ShapeCount;
        Shape.Item(1).Delete;
    end
end

% 绘图并放置于表格单元(8,1)
zft = figure('units','normalized','position',...
[0.280469 0.553385 0.428906 0.251302],'visible','off'); % 定义句柄
% 绘图
set(gca,'position',[0.1 0.2 0.85 0.75]);
data = normrnd(0,1,1000,1);
hist(data);
grid on;
xlabel('考试成绩');
ylabel('人数');

hgexport(zft, '-clipboard'); % 将图片复制到剪切板
DTI.Cell(8,1).Range.Paragraphs.Item(1).Range.PasteSpecial; % 粘贴操作
Shape.Item(1).WrapFormat.Type = 3;
Shape.Item(1).ZOrder('msoBringInFrontOfText');
delete(zft);    % 删除句柄

Document.ActiveWindow.ActivePane.View.Type = 'wdPrintView';
Document.Save;  % 保存文档
Word.Quit;      % 关闭文档

```