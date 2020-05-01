from .randaugment import RandAugmentMC

transform_labeled = transforms.Compose([
        transforms.RandomHorizontalFlip(),
        transforms.RandomVerticalFlip(),
        #transforms.RandomCrop(size=32,padding=int(32*0.125),padding_mode='reflect'),
        transforms.RandomRotation(180),
        transforms.ColorJitter(brightness=0.1, contrast=0.2,saturation=0.2, hue=0.02),
        transforms.RandomAffine(0, translate=(0.05,0.05), scale=(0.9,1.1), shear=10),
        transforms.ToTensor(),
        transforms.Normalize(norm['mean'], norm['std'])
    ])
transform_val = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(norm['mean'], norm['std'])
    ])

strong_augumentation = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.RandomVerticalFlip(),
            transforms.RandomRotation(180),
            #transforms.ColorJitter(brightness=0.1, contrast=0.2,saturation=0.2, hue=0.02),
            #transforms.RandomAffine(0, translate=(0.05,0.05), scale=(0.9,1.1), shear=10),
            #transforms.RandomCrop(size=32,padding=int(32*0.125),padding_mode='reflect'),
            RandAugmentMC(n=2, m=10),
            transforms.ToTensor(),
            transforms.Normalize(norm['mean'], norm['std'])])


weak_augumentation = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.RandomVerticalFlip(),
            transforms.RandomRotation(180),
            #transforms.ColorJitter(brightness=0.1, contrast=0.2,saturation=0.2, hue=0.02),
            #transforms.RandomAffine(0, translate=(0.05,0.05), scale=(0.9,1.1), shear=10),
            #transforms.RandomCrop(size=32,padding=int(32*0.125),padding_mode='reflect'),
            transforms.ToTensor(),
            transforms.Normalize(norm['mean'], norm['std'])])

weak_unlabel = datasets.ImageFolder(UNLABEL_DIR, transform = weak_augumentation)
strong_unlabel = datasets.ImageFolder(UNLABEL_DIR, transform = strong_augumentation)
weak_unlabel_loader = torch.utils.data.DataLoader(weak_unlabel, batch_size=1, shuffle=False)
strong_unlabel_loader = torch.utils.data.DataLoader(strong_unlabel, batch_size=1, shuffle=False)

'''Example
for epoch in range(epoch_num):
    
    for weak_unlabel_inputs, _ in weak_unlabel_loader:
    '''