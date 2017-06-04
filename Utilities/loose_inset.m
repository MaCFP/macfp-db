set(gca,'units','centimeters')
pos = get(gca,'Position');
li = get(gca,'LooseInset');
set(gcf, 'PaperUnits','centimeters');
set(gcf, 'PaperSize', [pos(3)+li(1)+li(3) pos(4)+li(2)+li(4)]);
set(gcf, 'PaperPositionMode', 'manual');
set(gcf, 'PaperPosition',[0.5 0.5 pos(3)+li(1)+li(3) pos(4)+li(2)+li(4)]);