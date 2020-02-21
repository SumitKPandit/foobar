from fractions import Fraction, gcd

def solution(m):

    def make_std(m):
        new_seq = []
        r_mat = []
        q_mat = []
        last_absorbing_idx = None
        for idx, row in enumerate(m):
            if sum(row) == 0:
                if last_absorbing_idx == None:
                    last_absorbing_idx = idx
                new_seq.insert(0, idx)
            else:
                new_seq.append(idx)
        last_absorbing_idx = new_seq.index(last_absorbing_idx)
        for row_idx, row in enumerate(new_seq):
            if row_idx > last_absorbing_idx:
                total = sum(m[row])
                new_row_r = []
                new_row_q = []
                for col_idx, col in enumerate(new_seq):
                    if col_idx <= last_absorbing_idx:
                        new_row_r.append(Fraction(m[row][col], total))
                    else:
                        new_row_q.append(Fraction(m[row][col], total))
                r_mat.append(new_row_r)
                q_mat.append(new_row_q)
        return (r_mat, q_mat)
    
    def find_adj(m):
        adj = []
        if len(m) == 1:
            if m[0][0] == 0:
                return 0
            return 1
        else:
            for i in range(len(m)):
                row_adj = []
                for j in range(len(m[i])):
                    minor = []
                    for k in range(len(m)):
                        row_minor = []
                        for l in range(len(m[k])):
                            if k != j and l != i:
                                row_minor.append(m[k][l])
                        if len(row_minor) != 0:
                            minor.append(row_minor)
                    sign = 1 if (i + j) % 2 == 0 else -1
                    val = Fraction(sign, 1) * find_det(minor)
                    row_adj.append(val)
                adj.append(row_adj)
        return adj
        
    def find_det(m):
        if len(m) == 1:
            return m[0][0]
        elif len(m) == 2:
            return (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
        else:
            det = Fraction(0, 1)
            for i in range(len(m[0])):
                minor = []
                for j in range(1, len(m)):
                    row_minor = []
                    for k in range(len(m[j])):
                        if k != i:
                            row_minor.append(m[j][k])
                    if len(row_minor) != 0:
                        minor.append(row_minor)
                sign = 1 if i % 2 == 0 else -1
                det += (Fraction(sign, 1) * m[0][i] * find_det(minor))
            return det
    
    def divide_mat(num, fac):
        result = []
        for row in num:
            row_result = []
            for elem in row:
                row_result.append(elem / Fraction(fac, 1))
            result.append(row_result)
        return result
    
    def find_f(q):
        pre_f = []
        for i in range(len(q)):
            row_pre_f = []
            for j in range(len(q[0])):
                if i == j:
                    row_pre_f.append(Fraction(1, 1) - q[i][j])
                else:
                    row_pre_f.append(Fraction(0, 1) - q[i][j])
            pre_f.append(row_pre_f)
            row_pre_f = []
        adj = find_adj(pre_f)
        det = find_det(pre_f)
        f_mat = divide_mat(adj, det)
        return f_mat
        
    def mul_mat(f_mat, r_mat):
        product = []
        for i in range(len(f_mat)):
            row_product = []
            for j in range(len(r_mat[0])):
                elem = Fraction(0, 1)
                for k in range(len(r_mat)):
                    elem += (f_mat[i][k] * r_mat[k][j])
                row_product.append(elem)
            product.append(row_product)
        return product
    
    def get_final(m):
        lcm = 1
        final_arr = []
        def get_lcm(m, n):
            return int((m * n) / gcd(m, n))
        for i in range(len(m[0])):
            lcm = get_lcm(lcm, m[0][i].denominator)
        for i in range(len(m[0]) - 1, -1, -1):
            final_arr.append(int(lcm / m[0][i].denominator) * m[0][i].numerator) 
        final_arr.append(lcm)
        return final_arr

    r_mat, q_mat = make_std(m)
    f_mat = find_f(q_mat)
    product = mul_mat(f_mat, r_mat)
    output = get_final(product)
    return output

def main():
    # test1 = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
    test2 = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    print(solution(test2))

main()