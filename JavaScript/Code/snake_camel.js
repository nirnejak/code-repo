let snake_case = 'snake_case_to_camel_case'
let camelCase = snake_case.split('_').map(ch => ch.replace(ch[0],ch[0].toUpperCase())).join('')
let humanize = snake_case.split('_').map(l => l[0].toUpperCase() + l.slice(1)).join(' ')
