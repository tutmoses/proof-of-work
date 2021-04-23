def POW(data,zeros,nonce): ##  CRYPTO  ##
    while True:
        combo = (str(data) + str(nonce)).encode("utf-8")
        hash_ = sha256(combo).hexdigest()
        if hash_.startswith(zeros * "0"):
            return nonce, hash_
        else:
            nonce += 1
