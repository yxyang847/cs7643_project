# Application of Fixmatch in transfer learning with respect to medical image classfication

We modify Fixmatch to make it applicable in transfer learning, specialized in medical image classfication
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

contact hwang787@gatech.edu, ztang316@gatech.edu, jxie315@gatech.edu or yixuyang@gatech.edu for huge size training & testing data.
If you want to use our model or code, make sure your folder structure is compatible with our customized dataset.py as well as dataloader. For more detailed, please read this
[vague and obscure tutorial on pytorch](https://pytorch.org/tutorials/beginner/data_loading_tutorial.html)


```
- Python 3.6+
- PyTorch 1.4
- torchvision 0.5
- tensorboard
- tqdm
- numpy
- apex (optional)
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo


### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Ziqi Tang** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)
* **Jiajia Xie** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)
* **Yixun Yang** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)
* **Hanchen Wang** - *Initial work* - [PurpleBooth](https://github.com/hwang787)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* A previously developed [randaugment.py](https://github.com/kekmodel/FixMatch-pytorch/blob/e867808ab317f64a449988ecb60c8271b677bcb3/dataset/randaugment.py) were implemented
```
@misc{lia_corrales_2015_15991,
    author       = {Jungdae Kim},
    title        = {{Unofficial PyTorch implementation of MixMatch: A Holistic Approach to Semi-Supervised Learning}},
    year         = 2020,
    version      = {1.0},
    publisher    = {Zenodo},
    url          = {https://github.com/kekmodel/FixMatch-pytorch/blob/e867808ab317f64a449988ecb60c8271b677bcb3/dataset/randaugment.py}
    }
```

* FixMatch: Simplifying Semi-Supervised Learning with Consistency and Confidence (https://github.com/YU1ut/MixMatch-pytorch)
```
@article{sohn2020fixmatch,
    title={FixMatch: Simplifying Semi-Supervised Learning with Consistency and Confidence},
    author={Kihyuk Sohn and David Berthelot and Chun-Liang Li and Zizhao Zhang and Nicholas Carlini and Ekin D. Cubuk and Alex Kurakin and Han Zhang and Colin Raffel},
    journal={arXiv preprint arXiv:2001.07685},
    year={2020},
}
```

