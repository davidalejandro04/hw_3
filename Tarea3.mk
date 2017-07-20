data_targets = Datos.dat
image_targets1 = t30.png t60.png
image_targets2 = planetas.png

Resultados_hw3.pdf : Resultados_hw3.tex $(image_targets1) planetas.png
	pdflatex $< && rm *.aux *.log 

$(image_targets1) : onda.py 
	python $<

$(image_targets2) : Plots_planetas.py $(data_targets)
	python $<

$(data_targets) : a.out
	./a.out

a.out : planetas.c
	cc planetas.c -lm -o a.out

clean :
	rm *.dat *.png a.out *.pdf *.tex *.log *.aux
