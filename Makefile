compile:
	pip install -r requirements.txt

clean:
	find .  -name *.pyc -delete
	find .  -name *.sw* -delete

run:
	python -m mlf projects.wx.metar
