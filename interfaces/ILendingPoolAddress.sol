// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

interface ILendingPoolAddress {
    function getLendingPool() external view returns (address);
}