from algorithms.Sort import Sort


class BucketSort(Sort):

    def __str__(self):
        return "Bucket Sort"

    def sort(self):
        if len(self.array) < 2: return
        n = 5
        max_ = max(self.array)
        min_ = min(self.array)
        range_ = (max_ - min_) / n

        bucket = {}
        steps = []
        for e in self.array:
            idx = int((e - min_) / range_)
            idx = idx if idx < n else n - 1
            if idx in bucket.keys():
                bucket[idx].append(e)
            else:
                bucket[idx] = [e]
            steps.append(e)

        bucket_items = [e for _, v in sorted(bucket.items()) for e in v]

        for e in self.array[:]:
            idx_bucket = bucket_items.index(e)
            idx_array = self.array.index(e)
            self.array[idx_bucket], self.array[idx_array] = self.array[idx_array], self.array[idx_bucket]
            self.steps.append(self.array[:])

        for _, v in sorted(bucket.items()):
            for i in range(1, len(v)):
                for j, e in enumerate(reversed(v[:i])):
                    if not e > v[i - j]:
                        break
                    ele1 = v[i - j]
                    ele2 = v[i - j - 1]
                    idx1 = self.array.index(ele1)
                    idx2 = self.array.index(ele2)
                    self.array[idx1], self.array[idx2] = self.array[idx2], self.array[idx1]
                    v[i - j], v[i - j - 1] = v[i - j - 1], v[i - j]
                    self.steps.append(self.array[:])
