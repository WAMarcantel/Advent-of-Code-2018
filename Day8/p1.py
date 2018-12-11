def read_input(file):
    input_file = open(file)

    list = []
    for line in input_file:

        if line[len(line) - 1] is "\n":
            line = (line[:len(line) - 1])

        list.append(line)
    return list


nums = list(map(lambda x: int(x), read_input("input")[0].split()))
print(nums)


def getMetadataSum(nums, index):
    if len(nums) == 0:
        return 0
    print("starting at: ", index)

    childrenCount = nums[index]
    index += 1
    print(index)
    metadataCount = nums[index]
    index += 1
    print(index)

    if childrenCount == 0:
        metadata = sum(nums[index:index + metadataCount])
    else:
        childrenVals = []
        for i in range(childrenCount):
            metadata, index = getMetadataSum(nums, index)
            print(index)
            childrenVals.append(metadata)

        metadata = 0

        for i in range(index, index + metadataCount):
            print(nums[i]-1)
            if nums[i]-1 < len(childrenVals):
                print(i, nums[i]-1, childrenVals[nums[i]-1], childrenVals)
                metadata += childrenVals[nums[i]-1]

    return metadata, index + metadataCount


print(getMetadataSum(nums, 0))
