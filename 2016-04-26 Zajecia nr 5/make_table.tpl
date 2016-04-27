<html>
<head>
	<meta charset="UTF-8">
</head>
<body>
<table>
	<thead>
		<th>No</th>
		<th>Task name</th>
		<th>Is already done?</th>
		<th>Actions</th>
	</thead>
	<tbody>
%for row in rows:
	<tr>
		<td>{{row[0]}}</td>
		<td>{{row[1][0]}}</td>
		<td><a href="/toggle/{{ row[0] }}">{{ u'\u2714' if row[1][1] else u'\u2718' }}</a></td>
		<td><a href="/del/{{ row[0] }}">Delete</a></td>
	</tr>
%end
	</tbody>
</table>
<form action="new" method="POST">
	<input type="text" name="task">
	<input type="submit" name="save" value="Save">
</form>

</body>
</html>