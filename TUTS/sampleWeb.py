#!/usr/bin/python2.7
import flask

app = flask.Flask(__name__)

@app.route("/test")
def sampleRoute():
	return """
		<HTML>
			<BODY>
				<H2> <font color="green"> Simple TEST <h2> Testy </h2> </font> </H2>
				<H2> <font color="green"> Simple TEST </font> </H2>
				<H2> <font color="green"> Simple TEST </font> </H2>
				<H2> <font color="red"> Simple TEST </font> </H2>
				<H2> <font color="green"> Simple TEST </font> </H2>
				<H2> <font color="green"> Simple TEST </font> </H2>
				<H2> <font color="yellow"> Simple TEST </font> </H2>
				<H2> <font color="green"> Simple TEST </font> </H2>
				<H2> <font color="green"> Simple TEST </font> </H2>

			</BODY>
		</HTML>
	"""

@app.route("/test/<num>")
def sampleRouteS(num):
	return """
		<HTML>
			<BODY>
				<H2> Simple TEST </H2>
				<H2> Test Unit: {} </H2>
			</BODY>
		</HTML>
	""".format(num)

if __name__ == "__main__":
	app.run()