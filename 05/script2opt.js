const fs = require('fs');
const infile = 'input.txt';

let contents = fs.readFileSync(infile, 'utf-8').trim().split('\n\n');

let s = contents.shift().split(':')[1].trim().split(/\s+/).map(Number);

contents.map(sec => {
    sec.split(':\n')[1].split('\n').forEach(l => {
        l = l.trim().split(/\s+/).map(Number);
        rmap.push({s: l[1], e: l[1] + l[2], t: l[0]});
    });
    return rmap;
})
    .reduce((accmap, rmap) => {
        let tmp = [];
        accmap.forEach(r1 => {
            rmap.forEach(r2 => {
                let [fs, fe] = [r1.e, r1.t + r1.e - r1.s];
                if (!((fs <= rs.s && rs.s < fs) || (fe < rs.e && rs.e <= fe))) return;
                tmp.push({
                    s: Math.max(fs, r2.s),
                    e: Math.min(fe, r2.e),
                    t: r.t + Math.max(fs, r2.s) - r2.s
                })
            });
        });
        return tmp;
    }, [{s: 0, e: Infinity, t: 0}]);

console.log(Math.min(...s));
