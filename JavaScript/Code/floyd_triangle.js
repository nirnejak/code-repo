const floyd = (max_row) => {
    let column_count = 1;
    let num = 1;
    for (i = 0; i < max_row; i++) {
        row = '';
        for (j = 0; j < column_count; j++) {
            row += ' ' + num;
            num++;
        }
        console.log(row);
        column_count++;
    }
}

floyd(5);